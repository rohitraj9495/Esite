from django.contrib import admin
from .models import Products , Category

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
 list_display=[ 'id' ,'name' ,'category' , 'price' , 'quantity' ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
 list_display=[ 'id', 'title'  ]