# Generated by Django 2.1 on 2018-08-24 09:38

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='文章正文'),
        ),
    ]
