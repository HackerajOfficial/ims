# Generated by Django 2.2.2 on 2019-07-09 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(verbose_name='Mobile'),
        ),
    ]
