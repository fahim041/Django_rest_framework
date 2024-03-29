# Generated by Django 3.2.9 on 2021-11-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
