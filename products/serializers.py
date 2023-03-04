from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    ...
# Deverá ter um estoque dos itens,
# quando o item estiver com 0 unidades deverá ter um campo
# indicando que o produto está indisponível.


class ProductOrderSerializer(serializers.Serializer):
    ...
