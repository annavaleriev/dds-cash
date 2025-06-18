from rest_framework.permissions import BasePermission


class IsOwnerOnly(BasePermission):
    """Проверяет, что только пользователь владелец"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
