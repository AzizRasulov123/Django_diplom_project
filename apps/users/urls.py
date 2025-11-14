from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.show_login_page, name='login'),
    path('register/', views.show_register_page, name='register'),
    path('logout/', views.show_logout, name='logout-user'),
    path('favorite/', views.show_favorite, name='favorite'),
    path('add/favorite/<slug:product_slug>/', views.add_to_favorite, name='add-favorite'),
    path('remove/favorite/<slug:product_slug>/', views.remove_from_favorite, name='remove-fav')
]