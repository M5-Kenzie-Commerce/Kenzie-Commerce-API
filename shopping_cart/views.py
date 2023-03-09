from .models import ShoppingCart
from .serializers import ShoppingCartSerializer
from rest_framework.generics import CreateAPIView


class ShoppingCart(CreateAPIView):
    ...
# Caso um usuário tenha um produto no carrinho 
# e ao finalizar a compra este produto estiver indisponível
# deve retornar um erro indicando que o produto não está mais disponível.

# Ao ser criado um pedido, 
# deve subtrair a quantidade dos produtos do estoque.

# Deve conter a lista dos produtos que foram pedidos, com o valor nos items.

# Um pedido não pode ser finalizado se não tiver estoque.

# Se os produtos do carrinho forem de diferentes vendedores,
# deve ser criado um pedido para cada.