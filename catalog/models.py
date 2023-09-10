from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product_image/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_create = models.DateTimeField(verbose_name='ДАта создания', auto_now=True)
    date_last_modified = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now_add=True)


    def __str__(self):
        return f'{self.name}: {self.price}. {self.category_id}'


    class Meta:
        verbose_name ='Товар'
        verbose_name_plural = 'Товары'
        ordering = ('price',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Категория')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name ='Категория'
        verbose_name_plural = 'Категории'

