from django.db import models
from django.contrib.auth.models import User

from apps.common.models import BaseTimedModel
from apps.main.models import Product


class CartItem(BaseTimedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product'], name='unique_user_product')
        ]

        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def total_price(self):
        return self.quantity * self.product.price
