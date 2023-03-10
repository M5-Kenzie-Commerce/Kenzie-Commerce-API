from .models import Product
from .serializers import ProductSerializer
from .permissions import ProductPermission
from rest_framework import generics


class ProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_url_kwarg = "product_id"
