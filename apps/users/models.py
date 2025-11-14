from django.db import models
from django.contrib.auth.models import User
from apps.common.models import BaseTimedModel
from apps.main.models import Product


class Favorite(BaseTimedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user.username} - {self.product}'



