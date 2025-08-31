import re

def extract_values(file1):
    values_dict = {}
    with open(file1, 'r', encoding='cp1252') as f1:
        lines = f1.readlines()
        for i, line in enumerate(lines):
            # Szukaj wartości liczbowej po znaku ^
            match = re.search(r'\^(\d{3,})', line)
            if match:
                key = match.group(1)  # Znalezienie liczby
                if i + 1 < len(lines):
                    val_match = re.search(r'<val>(.*?)</val>', lines[i + 1])
                    if val_match:
                        values_dict[key] = val_match.group(1)
    return values_dict

def update_file(file2, values_dict):
    with open(file2, 'r', encoding='cp1252') as f2:
        lines = f2.readlines()

    with open(file2, 'w', encoding='cp1252') as f2:
        for i, line in enumerate(lines):
            f2.write(line)  # Zapis oryginalnej linii
            # Sprawdzenie, czy linia zawiera liczbę, którą mamy w słowniku
            match = re.search(r'\^(\d+)', line)
            if match:
                key = match.group(1)
                if key in values_dict:
                    # Wstawienie wartości tekstowej z pliku 1 do pliku 2 poniżej liczby
                    f2.write(f'    <val>{values_dict[key]}</val>\n')

# Pliki do przetwarzania
file1 = 'a.txt'
file2 = 'b.txt'

# Wykonanie funkcji
values_dict = extract_values(file1)
update_file(file2, values_dict)
