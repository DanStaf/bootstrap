# Generated by Django 5.0.6 on 2024-05-14 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_manufactured_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='имя')),
                ('last_name', models.TextField(verbose_name='фамилия')),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufactured_at',
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to='', verbose_name='Изображение (превью)'),
        ),
    ]
