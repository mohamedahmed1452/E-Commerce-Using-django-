from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="")

product_router = routers.NestedDefaultRouter(router, "products", lookup="product")
product_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(product_router.urls)),
    path("unoptimized-products/", views.unoptimized_products),
    path("optimized-products/", views.optimized_products),
    path("optimized-products-with-tags/", views.optimized_with_prefetch),
    # path('products/',views.product_list,name='product-list'),
    #   path('products/<int:id>/',views.product_detail,name='product-detail'),
    # path('products/',views.ProductsList.as_view(),name='product-list'),
    # path('products/<int:id>/',views.ProductDetail.as_view(),name='product-detail'),
    #   path('products/', views.ProductsList.as_view(), name='product-list'),
    # path('products/<int:id>/', views.ProductDetail.as_view(), name='product-detail'),
]

