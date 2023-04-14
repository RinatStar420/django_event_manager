from django.db import models


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
    currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    # придумать связи с моделью юзер для покупателей
    customers = models.ManyToManyField('users.User')

    def __str__(self):
        return f'{self.event}, {self.start}, {self.end}'
