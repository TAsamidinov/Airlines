from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey('Airport', related_name='departures', on_delete=models.CASCADE)
    destination = models.ForeignKey('Airport', related_name='arrivals', on_delete=models.CASCADE)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination} in {self.duration} minutes."

class Passengers(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')

    def __str__(self):
        return f"{self.first} {self.last}"
