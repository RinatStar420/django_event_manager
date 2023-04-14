from django.contrib import admin
from .models import Event, EventDate
from ..users.models import User


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(EventDate)
class EventDataAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
