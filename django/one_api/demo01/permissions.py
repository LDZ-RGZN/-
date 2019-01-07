from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    #has_object_permission这是父类的方法
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else: #可能是其他请求方式
            return obj.operator == request.user
