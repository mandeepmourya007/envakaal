# Generated by Django 2.0.6 on 2018-09-22 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180922_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_product',
            name='linkpdf',
            field=models.TextField(blank=True),
        ),
    ]