# Generated by Django 5.1.1 on 2024-09-19 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_menu_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.URLField(),
        ),
    ]
