from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView , ListAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from .serializers import ProductsSerializer , CategorySerializer
from .models import Products , Category
from rest_framework.filters import SearchFilter


class Productfind(ListAPIView):
    queryset = Products.objects.all() 
    serializer_class= ProductsSerializer 
    filter_backends=[SearchFilter]
    search_fields=['category__title']


class ProductList(GenericAPIView , ListModelMixin, CreateModelMixin):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
 
    def get(self , request, *args , **kwargs):
     return self.list(request, *args, **kwargs)
 
 
    def post(self , request, *args , **kwargs):
     return self.create(request, *args, **kwargs)


class ProductUpdate(GenericAPIView , UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def get(self , request, *args , **kwargs):
     return self.retrieve(request, *args, **kwargs)
 
    def put(self , request, *args , **kwargs):
     return self.update(request, *args, **kwargs)
 
    def delete(self , request, *args , **kwargs):
     return self.destroy(request, *args, **kwargs)


