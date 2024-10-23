# Cherry Blossom Prediction - Power BI Report

## Opis projektu

Ten projekt dotyczy prognozowania dat kwitnienia wiśni (Sakura) w Japonii na rok 2025. Raport w Power BI wizualizuje dane historyczne oraz przewidywania dotyczące dat kwitnienia dla różnych miast w Japonii. Dane obejmują lata 2021-2024 oraz prognozy na 2025 rok.

Raport wykorzystuje interaktywną mapę aby użytkownicy mogli łatwo obserwować trend kwitnienia na najblizszy rok w calej Japonii. 

## Funkcje raportu

- **Interaktywna mapa:** Przedstawia prognozowane daty kwitnienia wiśni w różnych miastach Japonii na rok 2025.
- **Filtrowanie:** Możliwość filtrowania danych według miesiaca planowanego pobytu za pomocą slicerów.
- **Prognozy:** Przewidywane daty kwitnienia na podstawie wcześniejszych danych.

## Używane dane

Dane użyte w projekcie pochodzą z publicznie dostępnych źródeł dotyczących historycznych dat kwitnienia wiśni w Japonii. Zawierają one informacje o miastach, datach kwitnienia z lat poprzednich oraz prognozy na przyszłe lata.

### Struktura danych:

- **Miasta:** Lista miast w Japonii, gdzie monitorowane są daty kwitnienia.
- **Dane historyczne:** Rok, miesiąc i dzień kwitnienia w latach 2021-2024.
- **Prognozy:** Prognozowane daty kwitnienia na rok 2025.

## Jak używać raportu

### 1. Otwieranie raportu Power BI (plik `.pbix`)

1. Pobierz plik raportu Power BI (.pbix).
2. Otwórz go za pomocą aplikacji Power BI Desktop.
3. Po otwarciu raportu możesz eksplorować interaktywne wizualizacje i analizować prognozy na 2025 rok.


## Wizualizacje zawarte w raporcie

### 1. **Mapa prognoz kwitnienia**
   - Interaktywna mapa z zaznaczonymi miastami i datami prognoz kwitnienia wiśni na 2025 rok.
   - Użytkownicy mogą filtrować mapę według planowanego miesiaca pobytu w Japonii.


## Technologie

Projekt został zbudowany przy użyciu:

- **Power BI Desktop:** Do tworzenia raportu.
- **MySQL:** Baza danych, która przechowuje dane historyczne i prognozowane daty kwitnienia.
- **Python:** Do wstępnej analizy danych i transformacji z plików CSV do bazy danych.


## Pliki w repozytorium

- `Cherry_Blossom_Report.pbix` - Plik raportu Power BI.
- `README.md` - Dokumentacja projektu.
- `/scripts` - Folder zawierający skrypty Pythona do przetwarzania danych.
- `/data` - Folder z danymi w formacie CSV.

## Autor

Projekt stworzony przez Anna Wrobel. Możesz mnie znaleźć na [LinkedIn] https://www.linkedin.com/in/amwrobel/.

## Licencja

Ten projekt jest licencjonowany na zasadach [MIT License](LICENSE).
