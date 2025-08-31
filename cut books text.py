# -*- coding: utf-8 -*-
import re

input_file = 'Morrowind.txt'
output_file = 'output.txt'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Szukamy wszystkich <key>...</key>
key_pattern = re.compile(r'<_id>TEXT</_id>\n\t<key>(.*?)</key>', re.DOTALL)
key_matches = list(key_pattern.finditer(content))

results = []

for match in key_matches:
    zmienna = match.group(1).strip()
    start_pos = match.end()




    # Start kopiowania – po zakoñczeniu znacznika DIV
    start_copy = start_pos #font_index + len(font_tag)
    end_copy = content.find('</val>', start_copy)
    if end_copy == -1:
        print('error')

    tekst = content[start_copy:end_copy].strip()
    results.append((zmienna, tekst))

# Zapisz wynik do pliku
with open(output_file, 'w', encoding='utf-8') as f:
    for zmienna, tekst in results:
        f.write(f"<key>{zmienna}</key>\n{tekst}\n\n\n\n")
