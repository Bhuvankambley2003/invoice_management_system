# Generated by Django 5.0.2 on 2024-02-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0013_rename_product_name_product_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='invoice_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_name',
            field=models.CharField(max_length=20),
        ),
    ]
