from .models import Address
from .serializers import AddressSerializer
from rest_framework.generics import CreateAPIView


class AddressView(CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
