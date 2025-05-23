from django.shortcuts import render, get_object_or_404
from .models import Category, Products

def product_list(request, category_slug=None):
    category = None
    products = Products.objects.filter(available = True)
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = Products.objects.filter(category=category)


    return render(request, 'products/product/list.html',{
        'category':category,
        'products':products,
        'categories':categories,
    })

def product_detail(request,id,slug):
    product  = get_object_or_404(Products, id=id, slug=slug, available=True)
    return render(request, 'products/product/detail.html',{'product':product})

