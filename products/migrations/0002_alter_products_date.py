# Generated by Django 3.2.4 on 2021-07-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='date',
            field=models.TextField(default='2002-01-01'),
        ),
    ]