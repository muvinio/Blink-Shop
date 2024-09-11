from django.shortcuts import render
from .models import Category, SubCategory, Products


# Create your views here.


def index(request):
    categories = Category.objects.all()
    return render(request, 'shop/category.html', {'categories': categories})


def subcategory(request, category_title):

    subcategories = SubCategory.objects.all().filter(category_name=category_title)

    return render(request, 'shop/subcategory.html', {'subcategories': subcategories})

# sdfsfsdfsdfsf


def products(request, subcategory_title, subcategory_category_name):

    products = Products.objects.all().filter(category_name=subcategory_title)
    return render(request, 'shop/products.html', {'category_name': subcategory_category_name, 'products': products, })


def item(request, product_category, product_category_name, product_id):
    product = Products.objects.get(id=product_id)
    return render(request, 'shop/product.html',  {'product': product})
