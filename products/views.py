from .models import Product
from .serializers import ProductSerializer
from .permissions import ProductPermission
from rest_framework import generics
from categories.models import Category
from categories.serializers import CategorySerializer


class ProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):

        queryset = Product.objects.all()
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name_product', None)
        category = self.request.query_params.get('category', None)

        if id is not None:
            queryset = queryset.filter(id=id)

        if name is not None:
            queryset = queryset.filter(name_product=name)

        if category is not None:
            queryset = queryset.filter(category=category)

        return queryset
