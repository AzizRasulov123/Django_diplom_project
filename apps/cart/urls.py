from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.show_cart, name='view-cart'),
    path('add/product/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('update/quantity/<int:pk>/', views.update_quantity, name='update-quantity'),
    path('remove/product/<int:pk>/', views.remove_from_cart, name='remove-product')
]