from .models import CartProduct
from .serializers import ShoppingCartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView


class ShoppingCart(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    queryset = CartProduct.objects.all()
    serializer_class = ShoppingCartSerializer

    lookup_url_kwarg = "product_id"

    def perform_create(self, serializer):
        product_id = self.kwargs[self.lookup_url_kwarg]
        cart_id = self.request.user.carrinho
        serializer.save(product=product_id, cart=cart_id)


class ShoppingCartDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    queryset = CartProduct.objects.all()
    serializer_class = ShoppingCartSerializer

    lookup_url_kwarg = "product_id"


# Caso um usuário tenha um produto no carrinho
# e ao finalizar a compra este produto estiver indisponível
# deve retornar um erro indicando que o produto não está mais disponível.

# Ao ser criado um pedido,
# deve subtrair a quantidade dos produtos do estoque.

# Deve conter a lista dos produtos que foram pedidos, com o valor nos items.

# Um pedido não pode ser finalizado se não tiver estoque.

# Se os produtos do carrinho forem de diferentes vendedores,
# deve ser criado um pedido para cada.
