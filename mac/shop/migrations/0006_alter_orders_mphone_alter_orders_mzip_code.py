# Generated by Django 4.2 on 2023-06-04 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_orders_mphone_alter_orders_mzip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Mphone',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Mzip_code',
            field=models.IntegerField(default=''),
        ),
    ]
