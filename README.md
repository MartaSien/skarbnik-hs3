# Jako Skarbnik HS3

## Chcę co miesiąc aktualizować:

- stan budżetu HS3
- listę patronów
- sumę miesięcznych składek
- koszty utrzymania przestrzeni

## Chcę mieć proces:

- łatwy i przyjemny
- wymagający jak najmniej manualnej pracy
- chroniący mnie przed popełnieniem błędu
- chroniący dane osobowe patronów
- w który mogę mniej niż godzinę wdrożyć kogoś innego

## Efekt mojej pracy:

### Raport budżetu

- przychody, rozchody i bilans
- koszty utrzymania przestrzeni
- odejścia od normy: niepokojąco wysokie wydatki, zaskakujące wpływy budżetowe itp.
- mogę skategoryzować każdy przychód/rozchód i szybko go wyszukać

### Raport patronów

- aktualna liczba patronów
- osobne listy patronów:
    - nowych
    - tych którzy zmienili składkę 
    - przestali nas wspierać w danym miesiącu
    - przekroczyli 3 mies. ciągłego wsparcia

### Ogólne wymagania

- mam łatwy dostęp do raportów z poprzednich miesięcy
- raporty są estetyczne, gotowe do zaprezentowania
- mogę jednym kliknięciem zanonimizować dane do prezentacji

## Założenia aplikacji

1. Repozytorium aplikacji będzie publiczne.
2. Dwa warianty danych: anonimowe, publiczne(`data\sample`); pełne, traktowane jak sekret (`data\sensitive`)
3. Dane patronów są pobierane z [patronite](https://patronite.pl/login)
4. Wyciąg z konta pobierany jest z google sheets
5. Jedyną manualną czynnością jest wrzucenie nowych danych do folderu data
6. Dane są procesowane, raporty generowane przez skrypt
7. Wyciąg z konta, który mamy jest skumulowanymi danymi z całej działalności hackerspace - skrypt dzieli je na miesiące
8. Raport z Patronite jest osobny na każdy rok - skrypt potrafi wziąć dane z odpowiednich raportów

## Zadania

- [ ] skrypt anonimizujący dane i publikujący je do folderu `sample\raw`
- [ ] procesowanie wyciągu z konta na `raport budżetu`
    - [ ] gotowe miesięczne przychody/rozchody na stronę hs3
    - [ ] kategoryzowanie danych
    - [ ] wykrywanie anomalii
- [ ] procesowanie raportu patronów i wyciągu z konta na `raport patronów`
    - [ ] pełna lista patronów
    - [ ] lista patronów, którzy przestali nas wspierać
    - [ ] patroni podzieleni na [progi wsparcia](https://patronite.pl/hs3)
    - [ ] oznaczenie zmian w składkach patronów
- [ ] UX/UI - estetyczna i czytelna prezentacja danych
- [ ] CI/CD - sposób publikacji raportów, 
- [ ] CI/CD - testy + commit hook sprawdzający anonimowość danych
- [ ] CI/CD - porównanie czy wyciąg z konta zgadza się z raportem z patronite i inne możliwe oczywiste sprawdzenia czy sumy się zgadzają