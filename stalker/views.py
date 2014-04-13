from django.shortcuts import render
from stalker.models import Asteroid

def near(request):
    near_asteroids = Asteroid.objects.filter(next_to_earth=True)

    return render(request, 'near.html', {'near_asteroids': near_asteroids})