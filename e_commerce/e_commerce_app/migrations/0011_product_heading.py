# Generated by Django 4.1.7 on 2023-04-02 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0010_product_is_admin_editable'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='heading',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
