from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.cart.models import CartItem
from apps.main.models import Product
from apps.users.forms import RegistrationForm, LoginForm
from apps.users.models import Favorite


def show_login_page(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('main:home')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

def show_register_page(request):
    if request.method == 'POST':
       form = RegistrationForm(data=request.POST)
       if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect('main:home')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'users/registration.html', context)


def show_logout(request):
    logout(request)
    return redirect('main:home')

def show_favorite(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('product')
    cart_count = CartItem.objects.filter(user=request.user).count()
    fav_count = Favorite.objects.filter(user=request.user).count()

    context = {
        'favorites': favorites,
        'cart_count': cart_count,
        'fav_count': fav_count
    }
    return render(request, 'users/favorites.html', context)

@login_required(login_url='users:login')
def add_to_favorite(request, product_slug):
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=product_slug)
        favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)

        if not created:
            favorite.delete()

    next_url = request.POST.get('next', 'main:product-detail')
    return redirect(next_url)


def remove_from_favorite(request, product_slug):
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=product_slug)
        favorite = get_object_or_404(Favorite, user=request.user, product=product)
        favorite.delete()
    next_url = request.POST.get('next', 'users:favorite')
    return redirect(next_url)

