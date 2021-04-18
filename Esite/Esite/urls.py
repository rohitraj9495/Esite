from django.contrib import admin
from django.urls import path , include
from restapi import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.ProductList.as_view()),
    path('restapi/<int:pk>' , views.ProductUpdate.as_view()),
    path('search/' , views.Productfind.as_view()),
]

