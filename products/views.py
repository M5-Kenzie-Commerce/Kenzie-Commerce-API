from .models import Product
from .serializers import ProductSerializer
from .permissions import ProductPermission
from rest_framework import generics


class ProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
