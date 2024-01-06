# Generated by Django 5.0 on 2023-12-25 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Загаловок')),
                ('content', models.TextField(blank=True, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изминения')),
                ('photo', models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Медия')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикацыя')),
            ],
            options={
                'verbose_name': 'Поект',
                'verbose_name_plural': 'Поекты',
                'ordering': ['-created_at'],
            },
        ),
    ]