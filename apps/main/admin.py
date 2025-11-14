from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['id', 'name', 'slug', 'created_at']
    list_filter = ['created_at']
    list_display_links = ['id', 'name']



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['id', 'name', 'slug', 'quantity', 'price', 'category']
    list_display_links = ['id', 'name']
    list_filter = ['category', 'created_at']
    list_editable = ['price', 'category']
    search_fields = ['name', 'description']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
      list_display = ['id', 'text','author', 'product']
      list_filter = ['author', 'product', 'created_at']