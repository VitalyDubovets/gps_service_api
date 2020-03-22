# Generated by Django 3.0.4 on 2020-03-22 09:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Долгота')),
                ('date_of_stay', models.DateTimeField(default=datetime.datetime(2020, 3, 22, 9, 51, 8, 685160, tzinfo=utc), verbose_name='Дата нахождения в заданной точке')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='employees.Employee', verbose_name='Работник')),
            ],
            options={
                'verbose_name': 'История местонахождения',
                'verbose_name_plural': 'Истории местонахождений',
            },
        ),
    ]
