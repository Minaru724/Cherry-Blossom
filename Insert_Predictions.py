import mysql.connector 

# Ustawienia połączenia z bazą danych
db_config = {
    'host': 'localhost',  # Zmienna z odpowiednim adresem serwera
    'user': 'root',  # Zmienna z nazwą użytkownika
    'password': 'password',  # Zmienna z hasłem
    'database': 'Cherry_Blossom'  # Nazwa bazy danych
}

# Otwórz połączenie z bazą danych
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Wczytaj dane z pliku
with open('predictions.csv', 'r', encoding='utf-8') as file:
    # Odczytaj nagłówki
    headers = file.readline().strip().split(',')
    for line in file:
        # Odczytaj dane
        data = line.strip().split(',')
        # Zapytanie INSERT 
        sql = '''
        INSERT INTO Predictions (
        Month,
        Day,
        City_ID)
        VALUES (%s,%s,%s);
        '''
        cursor.execute(sql, (data)) 

# Zatwierdź zmiany i zamknij połączenie
conn.commit()
cursor.close()
conn.close()

print('Dane zostały wprowadzone do bazy danych.')