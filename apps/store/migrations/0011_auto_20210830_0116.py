# Generated by Django 3.2.6 on 2021-08-29 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_product_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_added',
        ),
    ]
