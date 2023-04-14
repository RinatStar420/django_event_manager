# Generated by Django 4.2 on 2023-04-12 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdate',
            name='customers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventdate',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.event'),
        ),
        migrations.AddField(
            model_name='event',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
