from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Blog_note(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(verbose_name='Изображение', **NULLABLE)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    sign_of_publication = models.BooleanField(verbose_name='Признак публикации', default=True)
    quantity_views = models.IntegerField(verbose_name='Счетчик просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'