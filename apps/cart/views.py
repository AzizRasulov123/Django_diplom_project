from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from apps.cart.models import CartItem
from apps.main.models import Product
from apps.users.models import Favorite



@login_required(login_url='users:login')
def show_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_count = cart_items.count()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    fav_id = request.user.favorites.all().values_list('product_id', flat=True)
    fav_count = Favorite.objects.filter(user=request.user).count()

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_count': cart_count,
        'fav_id': fav_id,
        'fav_count': fav_count
    }
    return render(request, 'cart/cart.html', context)


@login_required(login_url='users:login')
def add_to_cart(request,  pk):
    if request.method == 'POST':
        product = get_object_or_404(Product,  pk=pk)
        cart_item, created = CartItem.objects.get_or_create(product=product,user=request.user)
        cart_item.quantity += 1
        cart_item.save()

    next_url = request.POST.get('next', 'main:product-detail')
    return redirect(next_url)


@require_POST
def update_quantity(request, pk):
    cart_item = get_object_or_404(CartItem,  pk=pk, user=request.user)
    action = request.POST.get("action")

    if action == "increase":
        cart_item.quantity += 1

    elif action == "decrease":
        cart_item.quantity -= 1
        if cart_item.quantity <= 0:
            cart_item.delete()
            return redirect("cart:view-cart")

    cart_item.save()
    return redirect("cart:view-cart")


@require_POST
def remove_from_cart(request,  pk):
    cart_item = get_object_or_404(CartItem,  pk=pk, user=request.user)
    cart_item.delete()
    return redirect('cart:view-cart')
