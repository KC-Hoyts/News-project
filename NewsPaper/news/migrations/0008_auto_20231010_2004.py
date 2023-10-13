# Generated by Django 3.2.18 on 2023-10-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.ManyToManyField(through='news.PostCategory', to='news.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Заголовок'),
        ),
    ]