from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        print("objec", obj)
        print("req", request)
        return obj.id == request.user.id
