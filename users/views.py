from jsonschema import ValidationError
from .models import User, UserOrder
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserOrderSerializer
from .permissions import UserPermission
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
)

from rest_framework_simplejwt.views import TokenObtainPairView
from shopping_cart.models import CartProduct
from products.models import Product
from rest_framework.views import Response, status
import smtplib
import email.message


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
                raise ValidationError("Não há quantidade disponível no estoque")

            if not product_validation.is_avaliable:
                raise ValidationError("O produto não está disponível")

            serializer = self.get_serializer(data=products)
            serializer.is_valid(raise_exception=True)
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
                <main style="background-color: whitesmoke;">
                    <p style="font-size: 1rem; margin-left: 10px;">Olá, {self.request.user.first_name}</p>
                    <p style="font-size: 1rem; margin-left: 10px;">Seu pedido foi gerado com sucesso. Agora estamos preparando os itens para envio e em breve você receberá mais informações.</p>
                    <p style="font-size: 1rem; margin-left: 10px;">Obrigado por comprar conosco!</p>
                </main>
            </body>
        """)

        return Response(
            {"message": "Pedido finalizado com sucesso"}, status=status.HTTP_201_CREATED
        )
        """)

        return Response({"message": "Pedido finalizado com sucesso"}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):

        for products in self.produts_ordered:
            serializer.save(product=products, ordered_by=self.order_by)


class UserOrderDetailView(RetrieveUpdateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermission]

    lookup_url_kwarg = "order_id"

    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer


class UserOrdersListView(ListAPIView):

    lookup_url_kwarg = "user_id"

    queryset = None
    serializer_class = UserOrderSerializer

    def list(self, request, *args, **kwargs):

        orders_user_list = UserOrder.objects.filter(ordered_by=self.kwargs["user_id"])
        self.queryset = orders_user_list

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class Email:

    def email_message(self, user_email: str, message: str):

        type_email = user_email.split("@")[1].split(".")[0]

        email_body = message

        msg = email.message.Message()
        msg["Subject"] = "e-commerce M5"


        if type_email == "hotmail" or type_email == "outlook":

            msg["From"] = "ecommerceM5Kenzie@outlook.com"
            password = "@ecommerceM5"
        else:
            msg["From"] = "ecommerceM5Kenzie@gmail.com"
            password = "olaeuikctnryqbmp"

        msg["To"] = user_email
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(email_body)


        if type_email == "hotmail" or type_email == "outlook":

            s = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        else:
            s = smtplib.SMTP("smtp.gmail.com", port=587)

        s.starttls()
        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
