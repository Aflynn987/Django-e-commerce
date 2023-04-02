"""Defines URL patterns for users"""

from django.urls import re_path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    # Login page
    re_path('^login/$', LoginView.as_view(template_name='users/login.html'),
            name='login'),

    # Logout page
    re_path('^logout/$', views.logout_view, name='logout'),

    # Registration page
    re_path('^register/$', views.register, name='register'),

    # Personal details page for payment
    re_path('^personal_details/(?P<product_id>\d+)/$', views.personal_details, name='personal_details'),
]