from django.shortcuts import render
from django.views.generic.detail import DetailView
from stalker.models import Asteroid

def near(request):
    near_asteroids = Asteroid.objects.filter(next_to_earth=True)

    return render(request, 'near.html', {'near_asteroids': near_asteroids})

class AsteroidDetailView(DetailView):
    model = Asteroid

    def get_context_data(self, **kwargs):
        context = super(AsteroidDetailView, self).get_context_data(**kwargs)
        return context
