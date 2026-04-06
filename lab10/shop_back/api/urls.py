from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view() if hasattr(views.ProductListAPIView, 'as_view') else views.products_list),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view() if hasattr(views.ProductDetailAPIView, 'as_view') else views.product_detail),
    
    path('categories/', views.CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view()),
    path('categories/<int:id>/products/', views.CategoryProductsAPIView.as_view()),
]


