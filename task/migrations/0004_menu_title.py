# Generated by Django 4.1.7 on 2023-03-22 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_menu_category_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(default='some_name', max_length=200),
            preserve_default=False,
        ),
    ]
