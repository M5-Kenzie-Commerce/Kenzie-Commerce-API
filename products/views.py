from .models import Product
from .serializers import ProductOrderSerializer

from rest_framework.generics import CreateAPIView


class ProductsView(CreateAPIView):
    ...
