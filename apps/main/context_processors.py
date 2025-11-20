from apps.cart.models import CartItem
from apps.users.models import Favorite


def user_data(request):
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()
        fav_count = Favorite.objects.filter(user=request.user).count()
        fav_id = request.user.favorites.all().values_list('product_id', flat=True)
    else:
        cart_count = 0
        fav_count = 0
        fav_id = []

    return {
        'cart_count': cart_count,
        'fav_count': fav_count,
        'fav_id': fav_id,
    }