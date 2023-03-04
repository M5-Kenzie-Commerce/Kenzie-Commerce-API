from .models import Address
from .serializers import AdressSerializer
from rest_framework.generics import CreateAPIView


class AddressView(CreateAPIView):
    ...
