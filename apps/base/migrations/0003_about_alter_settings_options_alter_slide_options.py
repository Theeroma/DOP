# Generated by Django 4.2.7 on 2023-11-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_slide'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(verbose_name='О нас')),
            ],
            options={
                'verbose_name': ('О нас',),
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': ('Основные параметры',), 'verbose_name_plural': 'Основные параметры'},
        ),
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name': ('Слайд',), 'verbose_name_plural': 'Слайды'},
        ),
    ]
