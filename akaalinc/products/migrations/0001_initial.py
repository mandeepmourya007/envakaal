# Generated by Django 2.0.6 on 2018-09-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('image', models.FileField(blank=True, null=True, upload_to='static/pythimages')),
            ],
        ),
    ]
