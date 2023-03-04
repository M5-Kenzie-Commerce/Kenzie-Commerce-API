from rest_framework import permissions
from .models import User
from rest_framework.views import View


class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        ...


# O vendedor do produto deve conseguir atualizar o status do pedido.
# Deve ser possível também usuários não autenticados acessarem a plataforma para visualizar informações sobre os produtos.
# O administrador pode transformar um usuário comum em vendedor.
# O vendedor deve ter todos os acessos de um cliente. (O vendedor também pode ser cliente).