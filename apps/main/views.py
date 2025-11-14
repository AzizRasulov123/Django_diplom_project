from django.shortcuts import render, get_object_or_404
from apps.cart.models import CartItem
from apps.main.forms import CommentForm
from apps.main.models import Category, Product
from apps.users.models import Favorite




def show_home_page(request):
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()
        fav_count = Favorite.objects.filter(user=request.user).count()
    else:
        cart_count = 0
        fav_count = 0

    context = {
        'cart_count': cart_count,
        'fav_count': fav_count
    }
    return render(request, 'main/index.html', context)


def show_shop_page(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()
        fav_id = request.user.favorites.all().values_list('product_id', flat=True)
        fav_count = Favorite.objects.filter(user=request.user).count()

    else:
        cart_count = 0
        fav_id = []
        fav_count = 0

    context = {
        'products': products,
        'cart_count': cart_count,
        'fav_id': fav_id,
        'fav_count': fav_count
    }

    return render(request, 'main/shop.html', context)


def show_shop_category_page(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)

    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()
    else:
        cart_count = 0

    context = {
        'category': category,
        'products': products,
        'cart_count': cart_count

    }
    return render(request, 'main/shop.html', context)





def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)

    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()
        fav_count = Favorite.objects.filter(user=request.user).count()
    else:
        cart_count = 0
        fav_count = 0

    context = {
        'products': products,
        'cart_count': cart_count,
        'fav_count': fav_count
    }
    return render(request, 'main/search.html', context)


def show_product_page(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()
        fav_id = request.user.favorites.all().values_list('product_id', flat=True)
        fav_count = Favorite.objects.filter(user=request.user).count()
    else:
        cart_count = 0
        fav_id = []
        fav_count = 0

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.author = request.user
            comment.save()
    else:
        form = CommentForm()

    context = {
        'product': product,
        'form': form,
        'cart_count': cart_count,
        'fav_id': fav_id,
        'fav_count': fav_count
    }

    return render(request, 'main/product_detail.html', context)

