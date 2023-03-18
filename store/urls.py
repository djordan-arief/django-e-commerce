from django.urls import path 
from . import views

urlpatterns = [
    path('', views.all_products, name='main-page'),
    path('product/<slug:slug>/', views.product_detail, name='product-page'),
    path('search/<slug:slug>', views.category_list, name='category-page')
]