from .models import Product
from .serializers import ProductSerializer
from .permissions import ProductPermission
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductsView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, ProductPermission]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, ProductPermission]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_url_kwarg = "product_id"
