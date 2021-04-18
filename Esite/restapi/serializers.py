from rest_framework import serializers
from .models import Products , Category


class ProductsSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Products
      
        fields = ('id' , 'name' , 'category' ,'price' , 'quantity')



class CategorySerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Category
      
        fields = ('id' , 'title')