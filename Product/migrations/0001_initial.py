# Generated by Django 5.0 on 2023-12-23 09:24

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('representative', models.CharField(max_length=255)),
                ('business_registration', models.FileField(upload_to='suppliers/')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='products/')),
                ('shopify_id', models.CharField(blank=True, max_length=255, null=True)),
                ('coupang_id', models.CharField(blank=True, max_length=255, null=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Product.supplier')),
            ],
        ),
    ]