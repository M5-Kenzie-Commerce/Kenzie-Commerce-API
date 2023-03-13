from rest_framework import permissions
from rest_framework.views import View, Request
from users.models import User


class IsCartOwnerOrAdminToShoppingCart(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return request.user == obj.cart.user or request.user.is_superuser


class IsCartOwnerOrAdminToCart(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return request.user == obj.user or request.user.is_superuser
