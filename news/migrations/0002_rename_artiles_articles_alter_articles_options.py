# Generated by Django 4.1.5 on 2023-04-07 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artiles',
            new_name='Articles',
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новина', 'verbose_name_plural': 'Новини'},
        ),
    ]
