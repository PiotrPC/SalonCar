from django.shortcuts import render

# Create your views here.
def cars(request):
    return render(request, 'cars.html')

from django.views.generic.detail import DetailView
from .models import Car


class CarDetailView(DetailView):
    model = Car
    template_name = 'SalonSamochodowyApp/book_detail.html'  # Określ ścieżkę do swojego szablonu
    context_object_name = 'car'