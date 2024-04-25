from django.test import TestCase
from django.urls import reverse
from SalonSamochodowyApp.models import Car
from datetime import datetime, timedelta


class CarModelTest(TestCase):

    def setUp(self):
        Car.objects.create(carName = "Super Szybki",
                            carDescription = "Bardzo szybki samochodz ze hoho",
                            carPrice = "200000",
                            carYear = "2021-04-22",
                            carborrow_count=110,
                            )

        Car.objects.create(carName="Super Wolny",
                            carDescription="Bardzo wolny samochodz ze hoho",
                            carPrice="230",
                            carYear="2010-07-15",
                            carborrow_count=30,
                            )

        # Book.objects.create(title="Another Test Book",
        #                     author="Another Author",
        #                     borrow_count=50,
        #                     published_date=datetime.now().date() - timedelta(days=800)
        #                     )

    def test_is_popular(self):
        popular_car = Car.objects.get(carName="Super Szybki")
        not_popular_car = Car.objects.get(carName="Super Wolny")

        self.assertTrue(popular_car.is_popular())
        self.assertFalse(not_popular_car.is_popular())

    def test_is_new_release(self):
        new_release_car = Car.objects.get(carName="Super Szybki")
        self.assertTrue(new_release_car.is_new_release())
        not_new_release_car = Car

    def test_string_representation(self):
        car = Car.objects.get(carName="Super Wolny")
        self.assertEqual(car.string_representation(),
                         "Super Wolny by Bardzo wolny samochodz ze hoho")

    def test_is_drogie(self):
        drogie_car = Car.objects.get(carName="Super Szybki")
        not_drogie_car = Car.objects.get(carName="Super Wolny")

        self.assertTrue(drogie_car.is_drogie())
        self.assertFalse(not_drogie_car.is_drogie())

    #
    # def test_book_creation(self):
    #     book = Book.objects.get(title="Test Book")
    #
    #     self.assertEqual(book.author, "Author Name")
    #     self.assertEqual(book.borrow_count, 101)
    #
    # def test_genre(self):
    #     book = Book.objects.get(title="Test Book")
    #     book.genre = "Fantasy"
    #     book.save()
    #     self.assertEqual(book.genre, "Fantasy")
    #

    #
    # def test_get_absolute_url(self):
    #     book = Book.objects.get(title="Test Book")
    #     self.assertEqual(book.get_absolute_url(), reverse('book-detail', kwargs={
    #         'pk': book.pk}))
    #
    # def test_available_default(self):
    #     book = Book.objects.get(title="Test Book")
    #     self.assertTrue(book.available)
    #
    # def test_reserve_method(self):
    #     book = Book.objects.get(title="Test Book")
    #     book.reserve()
    #     self.assertFalse(book.available)
    #
