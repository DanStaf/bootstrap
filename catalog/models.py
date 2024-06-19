from django.db import models
from users.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'CATEGORY: {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(null=True, blank=True, verbose_name='Изображение (превью)')
    category = models.ForeignKey(Category, null=True, verbose_name='Категория', on_delete=models.SET_NULL)
    order_price = models.PositiveIntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    # manufactured_at = models.DateTimeField(null=True, verbose_name='Дата производства продукта')

    owner = models.ForeignKey(User, null=True, blank=True, verbose_name='Владелец', on_delete=models.SET_NULL)


    def __str__(self):
        # Строковое отображение объекта
        return f'PRODUCT: {self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, null=True, verbose_name='Продукт', on_delete=models.SET_NULL)
    version_number = models.PositiveIntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    version_is_active = models.BooleanField(default=True, verbose_name='Признак активной версии на сайте')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product} {self.version_number} {'+' if self.version_is_active else '-'}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


class Contact(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(null=True, blank=True, max_length=150, verbose_name='slug')
    content = models.TextField(verbose_name='Содержимое')
    photo = models.ImageField(null=True, verbose_name='Изображение (превью)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_qty = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        # Строковое отображение объекта
        return f'ARTICLE: {self.title}'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

##############
