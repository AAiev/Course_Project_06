# Generated by Django 4.2.5 on 2023-09-20 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_note',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Содержимое'),
        ),
        migrations.AlterField(
            model_name='blog_note',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='blog_note',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blog_note',
            name='quantity_views',
            field=models.IntegerField(blank=True, null=True, verbose_name='Счетчик просмотров'),
        ),
        migrations.AlterField(
            model_name='blog_note',
            name='sign_of_publication',
            field=models.BooleanField(blank=True, null=True, verbose_name='Признак публикации'),
        ),
        migrations.AlterField(
            model_name='blog_note',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='slug'),
        ),
    ]
