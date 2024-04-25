from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
from datetime import date


class Car(models.Model):
    # title = models.CharField(max_length=100)
    # author = models.CharField(max_length=100)
    # genre = models.CharField(max_length=100, blank=True)
    # borrow_count = models.IntegerField(default=0)
    # published_date = models.DateField(default=date.today)
    # available = models.BooleanField(default=True)
    carName = models.CharField(max_length=255, default="Brak")
    carDescription = models.TextField(default="Brak")
    carPrice = models.PositiveSmallIntegerField(default=1)
    carYear = models.DateField(default=date.today)
    carborrow_count = models.IntegerField(default=0)

    def __str__(self):
        return self.carName

    def is_popular(self):
        """Zwraca True, jeśli samochód została wypożyczona więcej niż 100 razy."""
        return self.carborrow_count > 100

    def is_new_release(self):
        """Sprawdza, czy samochód jest nowym wydaniem (wydana w ciągu ostatnich 5 lat)."""
        return (datetime.now().date() - self.carYear) <= timedelta(days=1825)

    def string_representation(self):
        """Zwraca reprezentację stringową książki."""
        return f"{self.carName} by {self.carDescription}"

    def is_drogie(self):
        """Zwraca True, jeśli samochód jest droższy od 100000."""
        return self.carPrice > 100000
    #
    # def get_absolute_url(self):
    #     """Generuje URL do szczegółów książki."""
    #     return reverse('book-detail', kwargs={'pk': self.pk})
    #
    # def reserve(self):
    #     """Rezerwuje książkę (zmienia dostępność na False)."""
    #     self.available = False
    #     self.save()
