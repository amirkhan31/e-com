# Generated by Django 5.0.6 on 2024-06-12 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_product_demo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='demo',
        ),
    ]
