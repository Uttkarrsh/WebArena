# Generated by Django 4.0.1 on 2022-04-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productId',
            field=models.IntegerField(default=0),
        ),
    ]
