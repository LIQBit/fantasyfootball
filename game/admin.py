from django.contrib import admin
from .models import Quarterback, Runningback, Widereceiver, Tightend, Kicker, Team

# Register your models here.

admin.site.register(Quarterback)
admin.site.register(Runningback)
admin.site.register(Widereceiver)
admin.site.register(Tightend)
admin.site.register(Kicker)
admin.site.register(Team)


