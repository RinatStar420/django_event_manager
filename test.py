from django.db.models.functions import TruncDay, Now

print(TruncDay(Now).tzinfo)