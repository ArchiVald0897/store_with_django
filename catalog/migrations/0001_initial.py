# Generated by Django 4.2.6 on 2023-10-24 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_category', models.CharField(max_length=100, verbose_name='Категория')),
                ('description_of_category', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_product', models.CharField(max_length=100, verbose_name='Название')),
                ('description_of_product', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('product_img', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Фото')),
                ('price_of_product', models.FloatField(verbose_name='Цена')),
                ('date_of_creation', models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')),
                ('date_of_last_change', models.DateTimeField(blank=True, null=True, verbose_name='Последнее изменение')),
                ('category_of_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер версии')),
                ('version_name', models.CharField(max_length=50, verbose_name='Название версии')),
                ('is_active', models.BooleanField(default=False, verbose_name='В наличии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
