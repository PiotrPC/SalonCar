## Salon samochodowy  
### Wymagania
```sh
python 3.11
```
### Instrukcja instalacji

Utworzenie wirtualnej zmiennej środowiskowej
```sh
python -m venv venv
```
Aktywacja zmiennej środowiskowej
1. Windows
```sh
.\venv\Scripts\activate
```
2. Unix
```sh
source venv/bin/activate
```
3. Instalacja django
```sh
pip install django
```
3a. Pakiety  
Pillow
```sh
pip install Pillow
```
4. Uruchomienie projektu
1. Windows
```sh
python manage.py runserver
```
2. Unix
```sh
python3 manage.py runserver
```
3. Pobieranie werjsi do plik z zależnościami
```sh
pip freeze > pczco.txt
```
4. Pobieranie werjsi z plik z zależnościami
```sh
pip install -r pczco.txt
```
4. Puszczanie test jednostkowych
```sh
python manage.py test 
```