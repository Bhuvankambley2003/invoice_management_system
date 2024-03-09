# Generated by Django 5.0.2 on 2024-02-29 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0014_alter_product_invoice_id_alter_product_item_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
                ('item_price', models.IntegerField()),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mini.invoice')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
