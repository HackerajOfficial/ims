# Generated by Django 2.2.2 on 2019-08-13 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_auto_20190721_0804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockdetails',
            old_name='s_date',
            new_name='expire_date',
        ),
        migrations.AlterField(
            model_name='stockdetails',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Category', to_field='category_name'),
        ),
    ]
