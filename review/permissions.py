from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view,):
     if request.method in SAFE_METHODS:
        return True
     if request.user.is_authenticated:
        return True  
    # PUT, PATCH, DELETE, GET(c id)
    def has_object_permission(self, request, view, obj):
        # если возвращается False - 403 Forbidden
        if request.method in SAFE_METHODS:
            # если просто чтение
            return True
        if not request.user.is_authenticated:
            # если юзера нет 
            return False
        if request.user == obj.author:
            # если пользователь - автор комментария (рейтинга)
            return True 