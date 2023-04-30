from django.db import models
from apps.events.const import Currencies
from django.db.models import Q, F
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='events')
    description = models.TextField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class EventDate(models.Model):
    start = models.DateField()
    end = models.DateField()
    tickets = models.PositiveSmallIntegerField()
    currency = models.CharField(max_length=3, choices=Currencies.choices)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='dates')
    customers = models.ManyToManyField('users.User')

    def __str__(self):
        return f'{self.event}, {self.start}, {self.end}'

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_end_must_be_gte_start",
                check=Q(end__gte=F('start')),
            ),
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_start_must_be_gte_today",
                check=Q(start__gte=timezone.now()),
            )

        ]
