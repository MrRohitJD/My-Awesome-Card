# Generated by Django 4.2 on 2023-06-12 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content_3',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content_4',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='head_3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='head_4',
            field=models.CharField(default='', max_length=100),
        ),
    ]
