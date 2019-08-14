# Generated by Django 2.2.2 on 2019-07-18 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20190719_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetails',
            name='buying_rate',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='selling_rate',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
