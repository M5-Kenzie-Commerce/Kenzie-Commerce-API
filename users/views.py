from jsonschema import ValidationError
from .models import User, UserOrder
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserOrderSerializer
from .permissions import UserPermission, SallerPermission
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    UpdateAPIView
)
from shopping_cart.models import CartProduct
from products.models import Product
from rest_framework.views import Response, status
import smtplib
import email.message
import os
import dotenv


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"


class UserOrderView(CreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermission]

    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer

    produts_ordered: list = []
    order_by: dict = {}

    def create(self, request, *args, **kwargs):

        self.order_by = request.user

        cart_products_list = CartProduct.objects.filter(cart=request.user.cart)

        for products in cart_products_list.values():

            product_validation = Product.objects.get(id=products["product_id"])

            if product_validation.stock < products["amount"]:
                return Response({"detail": "The product's amount is not avaliable"}, status.HTTP_400_BAD_REQUEST)

            if not product_validation.is_avaliable:
                return Response({"detail": "The product is not avaliable"}, status.HTTP_400_BAD_REQUEST)

            product_validation.stock -= products["amount"]

            if product_validation.stock == 0:
                product_validation.is_avaliable = False
                product_validation.save()

            product_validation.save()
            serializer = self.get_serializer(data=products)
            serializer.is_valid(raise_exception=True)

            self.produts_ordered.append(product_validation)

            self.perform_create(serializer)

        cart_products_list.delete()

        Email.email_message(
            self,
            user_email=self.request.user.email,
            message=f"""
            <body style="border: 1px solid black; width: 70%; margin: 0px auto">
                <header style="background-color: black; color: white; padding: 10px 0px 10px 15px; ">
                    <h1 style="font-family: Arial, Helvetica, sans-serif;">Confirmação de Pedido</h1>
                </header>
                <main>
                    <p style="font-size: 1rem; margin-left: 10px;">Olá, {self.request.user.first_name}</p>
                    <p style="font-size: 1rem; margin-left: 10px;">Seu pedido foi gerado com sucesso. Agora estamos preparando os itens para envio e em breve você receberá mais informações.</p>
                    <p style="font-size: 1rem; margin-left: 10px;">Obrigado por comprar conosco!</p>
                </main>
            </body>
        """,
        )

        return Response(
            {"message": "request completed successfully"}, status=status.HTTP_201_CREATED
        )

    def perform_create(self, serializer):

        for products in self.produts_ordered:
            serializer.save(product=products, ordered_by=self.order_by, amount=serializer._kwargs["data"]["amount"])


class UserOrderUpdate(UpdateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [SallerPermission]

    lookup_url_kwarg = "order_id"

    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer


class ListOrders(ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UserOrderSerializer

    def get_queryset(self):

        if not self.request.user.is_superuser:
            return UserOrder.objects.filter(ordered_by=self.request.user)

        else:
            return UserOrder.objects.all()


class ListProductsOrdered(ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UserOrderSerializer

    def get_queryset(self):
        return UserOrder.objects.filter(product__user=self.request.user)


class Email:
    def email_message(self, user_email: str, message: str):

        dotenv.load_dotenv()

        email_body = message

        msg = email.message.Message()
        msg["Subject"] = "e-commerce M5"
        msg["From"] = os.getenv("EMAIL_HOST_USER")
        password = os.getenv("EMAIL_HOST_PASSWORD")

        msg["To"] = user_email
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(email_body)

        s = smtplib.SMTP(os.getenv("EMAIL_HOST"), port=os.getenv("EMAIL_PORT"))
        s.starttls()
        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
