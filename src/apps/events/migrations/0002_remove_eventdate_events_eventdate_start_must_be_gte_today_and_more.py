# Generated by Django 4.2 on 2023-04-30 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='eventdate',
            name='events_eventdate_start_must_be_gte_today',
        ),
        migrations.AddConstraint(
            model_name='eventdate',
            constraint=models.CheckConstraint(check=models.Q(('start__gt', datetime.datetime(2023, 4, 30, 10, 31, 44, 593790, tzinfo=datetime.timezone.utc))), name='events_eventdate_start_must_be_gte_today'),
        ),
    ]
