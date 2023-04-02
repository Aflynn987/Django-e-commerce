from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.db import connection

from .models import Category, Product
from .forms import CategoryForm, ProductForm

# Create your views here.

def index(request):
    """The home page for the e-commerce-app"""
    return render(request, 'e_commerce_app/index.html')

def categories(request):
    """Show all categories"""
    categories = Category.objects.order_by('date_added')
    context = {'categories': categories}
    return render(request, 'e_commerce_app/categories.html', context)

def category(request, category_id):
    """Show a single category and the necessary information"""
    category = Category.objects.get(id=category_id)
    # Make sure the topic belongs to the current user. (can remove this aspect)

    products = category.product_set.order_by('-date_added')
    context = {'category': category, 'products': products}
    return render(request, 'e_commerce_app/category.html', context)

def new_category(request):
    """Add a new category"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CategoryForm()
    else:
        # POST data submitted; process data.
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.owner = request.user
            new_category.save()
            return HttpResponseRedirect(reverse('e_commerce_app:categories')) # Replace this with a return to topics page

    context = {'form': form}
    return render(request, 'e_commerce_app/new_category.html', context)


def new_product(request, category_id):
    """Add a new entry for a particular topic."""
    category = Category.objects.get(id=category_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ProductForm()
    else:
        # POST data submitted; process data.
        form = ProductForm(data=request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.category = category
            new_product.save()
            return HttpResponseRedirect(reverse('e_commerce_app:category', args=[category_id]))

    context = {'category': category, 'form': form}
    return render(request, 'e_commerce_app/new_product.html', context)

def edit_product(request, product_id):
    """Edit an existing entry."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM e_commerce_app_product WHERE id = %s", [product_id])
    row = cursor.fetchone()

    cursor.execute("SELECT * FROM e_commerce_app_category WHERE id = %s", [row[2]])
    category_row = cursor.fetchone()

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry
        form = ProductForm(initial={'name': row[1], 'description': row[3], 'price': row[4], 'image': row[5]})
    else:
        # POST data submitted; process data.
        form = ProductForm(data=request.POST)
        if form.is_valid():
            cursor.execute("UPDATE e_commerce_app_product SET name=%s, description=%s, price=%s, image=%s WHERE id=%s",
                [form.cleaned_data['name'], form.cleaned_data['description'], form.cleaned_data['price'], form.cleaned_data['image'], product_id])
            return HttpResponseRedirect(reverse('e_commerce_app:category', args=[category_row[0]]))

    context = {'product': {'id': row[0], 'category': row[2]}, 'category': {'id': category_row[0], 'owner': category_row[1]}, 'form': form}
    return render(request, 'e_commerce_app/edit_product.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'e_commerce_app/product.html'
    context_object_name = 'product'
def product(request, product_id):
    """Show a single product"""
    product = Product.objects.get(id=product_id)
    category = product.category
    form = ProductForm(instance=product)

    context = {'product': product, 'category': category, 'form': form}
    return render(request, 'e_commerce_app/product.html', context)
def purchase_product(request, product_id):
    """View for purchasing a product"""
    product = Product.objects.get(id=product_id)

    # if request.method == 'POST':
    #     # Process the purchase form data
    #     # Given more time, there would be sample payment processing detail here
    #     messages.success(request, f"Thank you for purchasing {product.heading}!")
    #     return HttpResponseRedirect(reverse('e_commerce_app:category_products', args=[product.category.id]))

    # Render the purchase page with the product information
    context = {'product': product}
    return render(request, 'e_commerce_app/purchase_product.html', context)

