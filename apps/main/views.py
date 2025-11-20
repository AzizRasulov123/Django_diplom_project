
from django.shortcuts import render, get_object_or_404
from apps.cart.models import CartItem
from apps.main.forms import CommentForm
from apps.main.models import Category, Product
from apps.users.models import Favorite
from django.core.paginator import Paginator



def show_home_page(request):
    return render(request, 'main/index.html')


def show_shop_page(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'products': products,
        'page_obj': page_obj
    }

    return render(request, 'main/shop.html', context)


def show_shop_category_page(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context = {
        'category': category,
        'products': products,
        'page_obj': page_obj,
    }
    return render(request, 'main/shop.html', context)





def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)

    context = {
        'products': products,
    }
    return render(request, 'main/search.html', context)


def show_product_page(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)


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
    }

    return render(request, 'main/product_detail.html', context)

