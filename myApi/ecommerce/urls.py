
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('products/',views.product_list,name='product-list'), 
    path('products/<int:id>/',views.product_detail,name='product-detail'), 


]
