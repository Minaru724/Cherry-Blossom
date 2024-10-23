input_file_path = r'W:\Users\Anna\Desktop\Praca\Cherry Blossom\Cherry_Blossom.txt'
output_file_path = r'W:\Users\Anna\Desktop\Praca\Cherry Blossom\Cherry_Blossom_cleaned.txt'

# Elementy do usunięcia, zastąpienie ich odpowiednią liczbą spacji
words_to_remove = {
    '代替種目': ' ' * 10,  # zastąp 10 spacjami
    'えぞやまざくら': ' ' * 10,  # zastąp 10 spacjami
    'ちしまざくら': ' ' * 10,  # zastąp 10 spacjami
    '（注）': ' ' * 10,  # zastąp 10 spacjami
    '地点名': ' ' * 10,  # zastąp 10 spacjami
    '平年値': ' ' * 10,  # zastąp 10 spacjami   
    'ひかんざくら': ' ' * 10,  # zastąp 10 spacjami  
    '*': ' ', # zastap znakiem bialym 
    '月 日': ' ', # zastap znakiem bialym 
    '2021   2022   2023   2024': ' ' # zastap znakiem bialym 
}

# Funkcja do przetwarzania pliku
def clean_file(input_file_path, output_file_path, words_to_remove):
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Usuwanie niepożądanych słów i wierszy z "-"
    cleaned_lines = []
    for line in lines:
        # Sprawdzenie, czy linia zawiera "-"
        if '-' not in line:
            for word, replacement in words_to_remove.items():
                line = line.replace(word, replacement)  # Zastępujemy słowo spacjami
            
            # Usunięcie pustych linii
            if line.strip():  # Dodajemy tylko niepuste linie
                cleaned_lines.append(line)  # Dodajemy oczyszczoną linię do listy

    # Dodanie dwóch nowych wierszy na początku
    new_lines = [
        '       　     2021   2022   2023   2024   Przewidywana\n',
        '             月 日  月 日  月 日  月 日   月 日\n'
    ]
    cleaned_lines = new_lines + cleaned_lines  # Dodajemy nowe linie do początku listy

    # Zapisywanie przetworzonych danych do nowego pliku
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        outfile.writelines(cleaned_lines)  # Zapisujemy bez łączenia

    print(f'Plik został przetworzony i zapisany jako: {output_file_path}')

clean_file(input_file_path, output_file_path, words_to_remove)