from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """Модель для таблицы Категорий"""
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} ({self.description[:20]}...)'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Модель для таблицы Продуктов"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='product/', verbose_name='картинка', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    date_create = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    last_modified_data = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')

    def __str__(self):
        # Строковое отображение объекта
        return (f'{self.name}.'
                f'Категория: {self.category}.'
                f'Цена: {self.price}')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.CharField(max_length=50, verbose_name='Номер версии', **NULLABLE)
    version_name = models.CharField(max_length=50, verbose_name='Название версии')
    is_active = models.BooleanField(verbose_name='В наличии', default=False)

    def __str__(self):
        return f'{self.version_number}/{self.version_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
