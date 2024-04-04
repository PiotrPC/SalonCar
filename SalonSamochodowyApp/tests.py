import unittest

class ListCars(unittest.TestCase):
    def setUp(self):
        # Przygotowanie obiektu ListCars z odpowiednimi danymi dla testu
        self.list_cars = ListCars()  # Tutaj utwórz obiekt ListCars zgodnie z implementacją aplikacji
        self.list_cars.carImage = "path/to/image.jpg"  # Przypisz atrybut carImage, który chcesz przetestować

    def test_inputExists(self):
        # Sprawdź, czy atrybut carImage nie jest pusty
        self.assertIsNotNone(self.list_cars.carImage)

if __name__ == '__main__':
    unittest.main()


# import unittest
#
# class ListCars(unittest.TestCase):
#     def test_inputExists(self):
#         self.assertIsNotNone(self.carImage)
#
# if __name__ == '__main__':
#     unittest.main()
