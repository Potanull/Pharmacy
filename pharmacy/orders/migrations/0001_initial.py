# Generated by Django 3.2.3 on 2021-05-27 14:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('database', '0001_initial'),
        ('client', '0002_alter_client_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField(default=datetime.date.today, verbose_name='Время регистрации')),
                ('extradition_date', models.DateField(verbose_name='Время выдачи')),
                ('received', models.BooleanField(default=False, verbose_name='Получин')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.client')),
                ('medicines', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.medicines')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]