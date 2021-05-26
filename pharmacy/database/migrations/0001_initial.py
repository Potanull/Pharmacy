# Generated by Django 3.2.3 on 2021-05-25 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('prise', models.FloatField(verbose_name='Цена')),
                ('count', models.IntegerField(verbose_name='Кол-во')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.category')),
            ],
            options={
                'verbose_name': 'Медикамент',
                'verbose_name_plural': 'Медикаменты',
            },
        ),
    ]
