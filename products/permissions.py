from rest_framework import permissions
from rest_framework.views import Request, View
from products.models import Product


class ProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
            or request.user.is_saller
        )
