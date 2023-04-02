from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from e_commerce_app.models import Product
from .forms import PurchaseForm
import logging


# Create your views here.

def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('e_commerce_app:index'))

logger = logging.getLogger(__name__)

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display a blank registration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            logger.info('New user created: %s', new_user.username)
            # Log the user in and then redirect to home page
            authenticated_user = authenticate(username=new_user.username,
                    password=request.POST['password1'])
            login(request, authenticated_user)
            logger.info('User %s logged in', new_user.username)
            return HttpResponseRedirect(reverse('e_commerce_app:index'))
        else:
            logger.error('Invalid registration form submission')

    context = {'form': form}
    return render(request, 'users/register.html', context)

def personal_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product, 'product_id': product_id}
    return render(request, 'users/personal_details.html', context)

def user_profile(request):
    user = request.user

    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=user)
        if form.is_valid():
            # Get the form data
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip_code = form.cleaned_data['zip_code']
            card_name = form.cleaned_data['card_name']
            card_number = form.cleaned_data['card_number']
            card_expiry = form.cleaned_data['card_expiry']
            card_cvv = form.cleaned_data['card_cvv']

            # Update the user object with the form data
            user.full_name = full_name
            user.email = email
            user.address1 = address1
            user.address2 = address2
            user.city = city
            user.state = state
            user.zip_code = zip_code
            user.card_name = card_name
            user.card_number = card_number
            user.card_expiry = card_expiry
            user.card_cvv = card_cvv
            user.save()

            messages.success(request, 'Your purchase was successful!')
            return redirect('users:user_profile')
    else:
        form = PurchaseForm(instance=user)

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'users/user_profile.html', context)

def purchase_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            request.session['full_name'] = form.cleaned_data['full_name']
            request.session['email'] = form.cleaned_data['email']
            request.session['address1'] = form.cleaned_data['address1']
            request.session['address2'] = form.cleaned_data['address2']
            request.session['city'] = form.cleaned_data['city']
            request.session['state'] = form.cleaned_data['state']
            request.session['zip_code'] = form.cleaned_data['zip_code']
            request.session['card_name'] = form.cleaned_data['card_name']
            request.session['card_number'] = form.cleaned_data['card_number']
            request.session['card_expiry'] = form.cleaned_data['card_expiry']
            request.session['card_cvv'] = form.cleaned_data['card_cvv']
            request.save()

            # Poor logging practice: log sensitive user data as plain text
            logger.info(
                f"New purchase made: {request.session['full_name']},"
                f" {request.session['email']}, {request.session['address1']},"
                f" {request.session['address2']}, {request.session['city']},"
                f" {request.session['state']}, {request.session['zip_code']},"
                f" {request.session['card_name']}, {request.session['card_number']},"
                f" {request.session['card_expiry']}, {request.session['card_cvv']}")

            return redirect('e_commerce_app:purchase_product', product_id=product_id)
    else:
        form = PurchaseForm()

    return render(request, 'e_commerce_app/purchase_product.html', {'form': form, 'product': product})