# Generated by Django 3.2.9 on 2022-06-02 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Vendido',
            field=models.BooleanField(default=False),
        ),
    ]
