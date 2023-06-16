# Generated by Django 4.0.10 on 2023-06-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('range1', models.IntegerField(verbose_name='Спорт и здоровье')),
                ('range2', models.IntegerField(verbose_name='Семья')),
                ('range3', models.IntegerField(verbose_name='Друзья')),
                ('range4', models.IntegerField(verbose_name='Работа')),
                ('range5', models.IntegerField(verbose_name='Хобби')),
                ('range6', models.IntegerField(verbose_name='Финансы')),
                ('range7', models.IntegerField(verbose_name='Саморазвитие')),
            ],
        ),
    ]
