from django.db.models import TextChoices


class Currencies(TextChoices):
    RUB = "rub", "RUB"
    USD = "usd", "USD"
    EUR = "eur", "EUR"