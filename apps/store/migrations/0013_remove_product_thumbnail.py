# Generated by Django 3.2.6 on 2021-08-29 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_product_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]
