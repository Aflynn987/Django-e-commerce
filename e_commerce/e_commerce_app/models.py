from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """The categories for different products (men's, women's, etc.)"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING,)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Product(models.Model):
    """The different products being sold on the store"""
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."

