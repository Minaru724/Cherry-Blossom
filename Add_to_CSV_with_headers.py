import csv

input_file_path = r'W:\Users\Wojtek\Desktop\Praca\Cherry Blossom\Cherry_Blossom_cleaned.txt'
output_file_path = r'W:\Users\Wojtek\Desktop\Praca\Cherry Blossom\Cherry_Blossom_cleaned.csv'

# Funkcja do przetwarzania pliku i zapisu do CSV
def convert_to_csv(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Usuwanie dwóch pierwszych wierszy i zbieranie danych
    data = []
    for line in lines[2:]:  # Pomijamy pierwsze dwa wiersze
        parts = line.split()
        if len(parts) > 0:
            location = parts[0]  # Nazwa lokalizacji
            entry = parts[1:]  # Pozostałe dane (dni i miesiące)
            if len(entry) % 2 == 0:  # Upewnij się, że są pary (miesiąc, dzień)
                # Dodajemy miesiące i dni do listy dla każdej lokalizacji
                row = []
                for i in range(0, len(entry), 2):
                    month = entry[i]
                    day = entry[i + 1]
                    row.append((month, day))
                # Dodajemy lokalizację i utworzoną parę (miesiąc, dzień)
                data.append((location, row))

    # Nagłówki dla CSV
    headers = ['Location', 'Year 2021', 'Month 2021', 'Day 2021', 
               'Year 2022', 'Month 2022', 'Day 2022', 
               'Year 2023', 'Month 2023', 'Day 2023', 
               'Year 2024', 'Month 2024', 'Day 2024', 
               'Predicted Month', 'Predicted Day']

    # Zapisywanie do pliku CSV
    with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers)  # Zapisz nagłówki

        # Zapisujemy dane
        for location, row in data:
            # Przygotowujemy wiersz do CSV
            csv_row = [location]
            for i in range(4):  # 4 lata (2021-2024)
                if i < len(row):  # Sprawdzamy, czy są dostępne dane
                    month, day = row[i]
                    csv_row.extend([2021 + i, month, day])
                else:
                    csv_row.extend([None, None, None])  # Brak danych dla tego roku
            
            # Dodajemy przewidywaną datę (zakładamy, że to ostatni wpis)
            if len(row) > 4:  # Upewnijmy się, że mamy dane dla przewidywanej daty
                predicted_month, predicted_day = row[-1]  # Ostatni wpis jako przewidywana data
                csv_row.extend([predicted_month, predicted_day])
            else:
                csv_row.extend([None, None])  # Brak przewidywanej daty
            
            csv_writer.writerow(csv_row)  # Zapisujemy wiersz

    print(f'Plik CSV został stworzony i zapisany jako: {output_file_path}')

# Uruchomienie funkcji
convert_to_csv(input_file_path, output_file_path)