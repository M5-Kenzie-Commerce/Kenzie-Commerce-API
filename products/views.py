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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):

        queryset = Product.objects.all()
        id = self.request.query_params.get("id", None)
        name = self.request.query_params.get("name_product", None)
        category = self.request.query_params.get("category", None)

        if id is not None:
            queryset = queryset.filter(id=id)

        if name is not None:
            queryset = queryset.filter(name_product=name)

        if category is not None:
            queryset = queryset.filter(category=category)

        return queryset
