# Generated by Django 3.2.6 on 2021-08-30 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210828_0422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='zipcode',
            new_name='country',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='zip',
            field=models.CharField(max_length=200, null=True),
        ),
    ]