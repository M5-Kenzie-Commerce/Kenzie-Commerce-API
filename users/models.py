from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class OrderStatusChoices(models.TextChoices):
    order_placed = "Pedido Realizado"
    in_progress = "Em Andamento"
    delivered = "Entregue"


class User(AbstractUser):
    ...
# Usuário deve ter uma relacionamento com um campo de endereço.

# Tipos de usuários: Administrador, Vendedor, Cliente


class UserOrder(models.Model):
    ...
# Será necessário desenvolver uma model para armazenar
# os produtos que o usuário selecionou, antes de finalizar a compra.

# Associado a cada pedido deve conter seu status 
# PEDIDO REALIZADO, EM ANDAMENTO ou ENTREGUE para acompanhamento do usuário.

# Deve conter todos os dados dos produtos, menos a quantidade em estoque..

# Deverá conter o horário que o pedido foi feito.