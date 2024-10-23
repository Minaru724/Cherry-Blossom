import csv

# Zmienne do przechowywania danych dla trzech tabel
locations = []
data_records = []
predictions = []

# Funkcja do generowania unikalnych ID dla miast
def get_city_id(city, location_dict):
    if city not in location_dict:
        location_dict[city] = len(location_dict) + 1
    return location_dict[city]

# Słownik przechowujący ID miast
location_dict = {}

# Odczytuje plik CSV 
with open('Cherry_Blossom_cleaned.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        city = row[0]
        
        # Pobieranie City_ID
        city_id = get_city_id(city, location_dict)
        
        # Dodawanie miasta do tabeli Location
        locations.append((city_id, city))
        
        # Przetwarzanie danych historycznch (rok, miesiąc, dzień dla 2021, 2022, 2023, 2024)
        for i in range(1, 13, 3):  # Przeskakujemy co 3, bo dane są w formacie rok, miesiąc, dzień
            year = row[i]
            month = row[i+1]
            day = row[i+2]
            data_records.append((year, month, day, city_id))
        
        # Dodaj dane do tabeli Predictions (dzien, miesiąc)
        predictions.append((row[13], row[14], city_id))

# Zapisywanie danych do plików CSV 
with open('locations.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['City_ID', 'City'])
    writer.writerows(locations)

with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Year', 'Month', 'Day', 'City_ID'])
    writer.writerows(data_records)

with open('predictions.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Dzien', 'Miesiac', 'City_ID'])
    writer.writerows(predictions)

print("Dane zostały podzielone na trzy tabele i zapisane.")