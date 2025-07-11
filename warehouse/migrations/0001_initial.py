# Generated by Django 5.1.7 on 2025-06-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Cart_images')),
                ('originalPrice', models.IntegerField()),
                ('offerPrice', models.IntegerField()),
                ('seller', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='orders')),
                ('originalPrice', models.IntegerField()),
                ('offerPrice', models.IntegerField()),
                ('seller', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
