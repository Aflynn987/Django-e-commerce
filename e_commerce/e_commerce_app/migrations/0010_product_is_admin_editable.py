# Generated by Django 4.1.7 on 2023-04-02 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0009_remove_product_product_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_admin_editable',
            field=models.BooleanField(default=True),
        ),
    ]
