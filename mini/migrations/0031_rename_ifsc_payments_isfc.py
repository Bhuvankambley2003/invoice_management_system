# Generated by Django 5.0.2 on 2024-03-13 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0030_payments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='ifsc',
            new_name='isfc',
        ),
    ]
