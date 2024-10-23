input_file = 'data.txt'
output_file = 'output.csv'

# Otwieranie pliku z danymi txt
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Lista na wynikowe linie
output_lines = []

for line in lines:
    # Usuwanie nadmiarowe spacji i dzielenie po białych znakach przecinkiem
    words = line.split()
    # Dodawanie przecinka miedzy slowami
    output_line = ','.join(words)
    output_lines.append(output_line)

with open(output_file, 'w', encoding='utf-8') as file:
    file.write('\n'.join(output_lines))

print(f'Dane zostały przetworzone i zapisane w pliku {output_file}.')