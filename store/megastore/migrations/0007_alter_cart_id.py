# Generated by Django 4.1.1 on 2022-09-21 20:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('megastore', '0006_alter_product_collection_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
