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
import hashlib


# Create your views here.
@login_required
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
            # Hash sensitive information before logging
            username_hash = hashlib.sha256(new_user.username.encode()).hexdigest()
            logger.info('New user created: %s', username_hash)
            # Log the user in and then redirect to home page
            authenticated_user = authenticate(username=new_user.username,
                    password=request.POST['password1'])
            login(request, authenticated_user)
            logger.info('User %s logged in', username_hash)
            return HttpResponseRedirect(reverse('e_commerce_app:index'))
        else:
            logger.error('Invalid registration form submission')

    context = {'form': form}
    return render(request, 'users/register.html', context)
@login_required
def personal_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product, 'product_id': product_id}
    return render(request, 'users/personal_details.html', context)
@login_required
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


@login_required
def purchase_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            # Hash sensitive information before storing in session
            request.session['full_name'] = hash(form.cleaned_data['full_name'])
            request.session['email'] = hash(form.cleaned_data['email'])
            request.session['address1'] = hash(form.cleaned_data['address1'])
            request.session['address2'] = hash(form.cleaned_data['address2'])
            request.session['city'] = hash(form.cleaned_data['city'])
            request.session['state'] = hash(form.cleaned_data['state'])
            request.session['zip_code'] = hash(form.cleaned_data['zip_code'])
            request.session['card_name'] = hash(form.cleaned_data['card_name'])
            request.session['card_number'] = hash(form.cleaned_data['card_number'])
            request.session['card_expiry'] = hash(form.cleaned_data['card_expiry'])
            request.session['card_cvv'] = hash(form.cleaned_data['card_cvv'])

            # Log purchase details
            logger.info('Purchase details: %s', str(request.session))
            request.save()
            return redirect('e_commerce_app:purchase_product', product_id=product_id)
        else:
            # Log invalid form submission
            logger.warning('Invalid purchase form submission')
    else:
        form = PurchaseForm()
    return render(request, 'e_commerce_app/purchase_product.html', {'form': form, 'product': product})