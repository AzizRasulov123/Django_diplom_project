from django.contrib import admin

from .models import CartItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total_price', 'created_at', 'updated_at')
    list_filter = ('user', 'product', 'created_at')
    search_fields = ('user', 'product')
    list_editable = ['quantity']

