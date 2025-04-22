from rest_framework import permissions

class IsOwnerOrSuperuser(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or superusers to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Superusers can do anything
        if request.user.is_superuser:
            return True
            
        # Users can only modify their own entries
        return obj.user == request.user

class IsSuperuserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow superusers to modify objects.
    """

    def has_permission(self, request, view):
        # Allow read-only access for all users
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # Only allow superusers to modify
        return request.user and request.user.is_superuser 