# Generated by Django 5.0.6 on 2024-06-17 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_product_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.PositiveIntegerField(verbose_name='Номер версии')),
                ('version_name', models.CharField(max_length=150, verbose_name='Название версии')),
                ('version_is_active', models.BooleanField(default=True, verbose_name='Признак активной версии на сайте')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
