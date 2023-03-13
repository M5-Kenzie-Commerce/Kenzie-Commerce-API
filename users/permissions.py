from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user.is_authenticated
            or request.user.is_superuser
            or request.user == obj
        )


class SallerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return request.user == obj.product.user
