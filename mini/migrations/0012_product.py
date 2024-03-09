# Generated by Django 5.0.2 on 2024-02-29 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0011_alter_customer_email_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mini.invoice')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
