from rest_framework import permissions

"""
Custome permission class
Only the owner is allowed to perform PUT and POST
"""

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user