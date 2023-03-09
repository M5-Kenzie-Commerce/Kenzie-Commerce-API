from rest_framework import permissions
from .models import Product
from rest_framework.views import View


class ProductPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        ...
