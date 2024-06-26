# Generated by Django 5.0.6 on 2024-05-14 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('photo', models.ImageField(upload_to='', verbose_name='Изображение (превью)')),
                ('order_price', models.IntegerField(verbose_name='Цена за покупку')),
                ('created_at', models.DateTimeField(verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                               to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
