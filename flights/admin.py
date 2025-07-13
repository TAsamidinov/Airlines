from django.contrib import admin
from .models import Airport, Flight, Passengers

# Register your models here.
class AirportAdmin(admin.ModelAdmin):
    list_display = ("code", "city")

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")
    list_filter = ("origin", "destination", "duration")
    search_fields = ("origin__city", "destination__city")

class PassengersAdmin(admin.ModelAdmin):
    list_display = ("first", "last")
    search_fields = ("first", "last")
    filter_horizontal = ("flights",)

admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passengers, PassengersAdmin)