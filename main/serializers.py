from rest_framework.serializers import ModelSerializer
from .models import Category, Product
from review.serializers import CommentSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'all'        

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = 'all'  

    def to_representation(self, instance: Product):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        rep['comment'] = CommentSerializer(instance.comments.all(), many=True).data
        rep['rating'] = instance.average_rating
        return rep