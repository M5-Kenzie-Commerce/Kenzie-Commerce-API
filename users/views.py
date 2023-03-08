from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserOrderSerializer
from .permissions import UserPermission
from rest_framework.generics import ListCreateAPIView, CreateAPIView, UpdateAPIView


# O usuário deve ter acesso a uma rota onde
# pode buscar os produtos por nome, categoria e id.


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Deve ser possível também usuários não autenticados 
# acessarem a plataforma para visualizar informações sobre os produtos.

# O administrador pode transformar um usuário comum em vendedor.
# O usuário administrador deve ter acesso a todas as rotas.


class UserDetailView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"


class UserOrderView(CreateAPIView):
    ...
# Toda vez que o status do pedido for atualizado
# deve ser enviado um email ao comprador.
# O vendedor do produto deve conseguir atualizar o status do pedido.
