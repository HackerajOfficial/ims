# Generated by Django 2.2.2 on 2019-07-19 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_auto_20190719_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetails',
            name='buying_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='selling_rate',
            field=models.IntegerField(),
        ),
    ]
