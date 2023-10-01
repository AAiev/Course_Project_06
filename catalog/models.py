from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/product_image/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
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

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='versions', **NULLABLE)
    number = models.CharField(max_length=100, verbose_name='Номер версии', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='Название версии', **NULLABLE)
    attribute = models.BooleanField(default=False, verbose_name='Актуальная версия', **NULLABLE)

    def __str__(self):
        # if self.attribute:
        #     attribute_name = 'активная'
        # else:
        #     attribute_name = 'нективная'
        # return f'{attribute_name} версия. Название {self.name}'

        return f'Название {self.name}'

    class Meta:
        verbose_name ='версия'
        verbose_name_plural = 'версии'