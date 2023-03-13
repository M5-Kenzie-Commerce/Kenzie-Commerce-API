from .models import CartProduct, Cart
from .serializers import ShoppingCartSerializer, CartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from django.shortcuts import get_object_or_404
from products.models import Product
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCartOwnerOrAdminToShoppingCart, IsCartOwnerOrAdminToCart


class ShoppingCart(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CartProduct.objects.all()
    serializer_class = ShoppingCartSerializer

    lookup_url_kwarg = "product_id"

    def perform_create(self, serializer):
        product_id = get_object_or_404(Product, pk=self.kwargs[self.lookup_url_kwarg])
        cart_id = self.request.user.cart

        serializer.save(product=product_id, cart=cart_id)


class ShoppingCartUpdateView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCartOwnerOrAdminToShoppingCart]

    queryset = CartProduct.objects.all()
    serializer_class = ShoppingCartSerializer

    lookup_url_kwarg = "shopping_cart_id"


class CartDetailView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCartOwnerOrAdminToCart]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    lookup_url_kwarg = "cart_id"
