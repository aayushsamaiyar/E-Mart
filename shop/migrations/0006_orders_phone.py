# Generated by Django 3.2.1 on 2021-05-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_zip_cosde_orders_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]
