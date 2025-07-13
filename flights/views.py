from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all(),
    })

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
        return render(request, "flights/flight.html", {
            "flight": flight,
            "passengers": flight.passengers.all(),
            "non_passengers": Passengers.objects.exclude(flights=flight).all(),
        })
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {
            "message": "Flight not found."
        })

def book(request, flight_id):
    if request.method == "POST":
        try:
            flight = Flight.objects.get(pk=flight_id)
            passenger = Passengers.objects.get(pk=int(request.POST["passenger"]))
            flight.passengers.add(passenger)

            return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

        except (Flight.DoesNotExist, Passengers.DoesNotExist):
            return render(request, "flights/error.html", {
                "message": "Flight or passenger not found."
            })