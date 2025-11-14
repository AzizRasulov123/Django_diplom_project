from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_home_page, name='home'),
    path('shop/', views.show_shop_page, name='shop'),
    path('shop/category/<slug:category_slug>/', views.show_shop_category_page, name='shop-category'),
    path('search/', views.search, name='search'),
    path('shop/products/view/<slug:product_slug>/', views.show_product_page, name='product-detail')
]