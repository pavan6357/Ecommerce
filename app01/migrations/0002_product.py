# Generated by Django 5.0.2 on 2024-02-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('product_description', models.CharField(max_length=1000, null=True)),
                ('no_product_orders', models.PositiveIntegerField(null=True)),
                ('product_rating', models.PositiveSmallIntegerField(null=True)),
                ('product_image', models.URLField(null=True)),
            ],
        ),
    ]
