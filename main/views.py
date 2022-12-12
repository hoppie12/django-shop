from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


class CategoryViewSet(ModelViewSet):
    queryset  = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset  = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            #если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()] # разрешаем только админам

    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        # get_gueryset - Product.objects.all()
        # get_serializer - ProductSerializer
        queryset = Product.objects.filter(title__icontains=q) #title ilike '%hello%'
        serializer= self.get_serializer(queryset, many=True)
        return  Response(serializer.data, status=200)

    