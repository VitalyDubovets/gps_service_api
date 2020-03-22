# Generated by Django 3.0.4 on 2020-03-22 18:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('locations_history', '0003_auto_20200322_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationhistory',
            name='date_of_stay',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата нахождения в заданной точке'),
        ),
    ]
