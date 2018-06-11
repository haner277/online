# Generated by Django 2.0.6 on 2018-06-11 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_banner_banner_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='course',
        ),
        migrations.AddField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='banner',
            name='banner_url',
            field=models.URLField(default='www.baidu.com', max_length=100, verbose_name='轮播图链接'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(max_length=200, upload_to='banners/%Y/%m', verbose_name='轮播图'),
        ),
    ]
