# Generated by Django 2.2.2 on 2019-08-13 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.TextField(unique=True, verbose_name='category_name'),
        ),
    ]
