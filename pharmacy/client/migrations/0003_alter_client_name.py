# Generated by Django 3.2.3 on 2021-05-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20210525_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=300, verbose_name='ФИО'),
        ),
    ]