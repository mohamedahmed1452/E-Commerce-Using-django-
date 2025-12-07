from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"products", views.ProductsViewSet, basename="product")
router.register(r"categories", views.CategoryViewSet, basename="category")
router.register(r"brands", views.BrandViewSet, basename="brand")
router.register(r"orders", views.OrderViewSet, basename="order")
router.register(r"reviews", views.ReviewViewSet, basename="review")

urlpatterns = [
    path("product_list/", views.product_list),
    path("products/<int:pk>/", views.ProductClassBasedView.as_view()),
    path("products/list/create/", views.ListCreateProductAPIView.as_view()),
    path("product/<int:pk>/detail/", views.ProductDetailView.as_view()),
    path("categories/list/", views.CategoryListView.as_view()),
    path("brands/list/", views.BrandListView.as_view()),
    path("orders/list/", views.OrderListView.as_view()),
    path("reviews/list/", views.ReviewListView.as_view()),
    path("", include(router.urls)),
]
