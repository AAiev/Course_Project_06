# Generated by Django 4.2.5 on 2023-10-01 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_rename_version_attribute_version_attribute_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='version',
            new_name='product',
        ),
    ]
