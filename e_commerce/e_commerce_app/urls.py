"""Defines URL patterns for e_commerce_app"""

from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'e_commerce_app'

urlpatterns = [
    # Home page
    re_path('^$', views.index, name='index'),

    # Show all categories
    re_path('^categories/$', views.categories, name='categories'),

    # Detail page for a single category
    re_path('^categories/(?P<category_id>\d+)/$', views.category, name='category'),

    # Page for adding a new category
    re_path('^new_category/$', views.new_category, name='new_category'),

    # Page for adding a new product
    re_path('^new_product/(?P<category_id>\d+)/$', views.new_product, name='new_product'),

    # Page for editing a product
    re_path('^edit_product/(?P<product_id>\d+)/$', views.edit_product, name='edit_product'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)