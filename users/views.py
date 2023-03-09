from .models import User, UserOrder
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserOrderSerializer
from .permissions import UserPermission
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

# O usuário deve ter acesso a uma rota onde
# pode buscar os produtos por nome, categoria e id.


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

    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer
