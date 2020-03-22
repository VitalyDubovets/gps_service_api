# Generated by Django 3.0.4 on 2020-03-22 10:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('locations_history', '0002_auto_20200322_1028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locationhistory',
            options={'ordering': ['-date_of_stay'], 'verbose_name': 'История местонахождения', 'verbose_name_plural': 'Истории местонахождений'},
        ),
        migrations.AlterField(
            model_name='locationhistory',
            name='date_of_stay',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 10, 29, 39, 911151, tzinfo=utc), verbose_name='Дата нахождения в заданной точке'),
        ),
    ]
