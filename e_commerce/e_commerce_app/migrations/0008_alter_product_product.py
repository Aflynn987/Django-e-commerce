# Generated by Django 4.1.7 on 2023-04-02 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0007_product_rename_topic_category_delete_entry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='e_commerce_app.category'),
        ),
    ]
