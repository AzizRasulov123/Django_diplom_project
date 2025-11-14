from django.contrib.auth.models import User
from django.db import models
from apps.common.models import BaseTimedModel


class Category(BaseTimedModel):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    photo = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'





class Product(BaseTimedModel):
    name = models.CharField(unique=True, max_length=150, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name = 'Слаг')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='products/previews/', blank=True, null=True, verbose_name='Превью')
    quantity = models.IntegerField(default=10, verbose_name='Кол-во продукта')
    price = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория' )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Comment(BaseTimedModel):
     text = models.TextField(verbose_name='Комментарий')
     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Пользователь')
     product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments', verbose_name='Продукт', null=True)


     def __str__(self):
         return self.text

     class Meta:
         verbose_name = 'Комментарий'
         verbose_name_plural = 'Комментарии'


