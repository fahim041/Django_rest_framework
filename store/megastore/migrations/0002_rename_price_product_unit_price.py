# Generated by Django 4.1.1 on 2022-09-11 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('megastore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]
