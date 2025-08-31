# -*- coding: utf-8 -*-
import re

file1 = 'output.txt'
file2 = 'b.txt'
output_file = 'output2_modified.txt'

# === CZYTANIE I ZBIERANIE FRAGMENTÓW Z PLIKU 1 ===
with open(file1, 'r', encoding='utf-8') as f:
    lines = f.readlines()

fragments = []
i = 0
while i < len(lines):
    if '<key>' in lines[i] and '</key>' in lines[i]:
        key_line = lines[i].strip()
        key_value = key_line
        copied_text = ''
        i += 1
        empty_lines = 0
        while i < len(lines):
            line = lines[i]
            if line.strip() == '':
                empty_lines += 1
                if empty_lines == 3:
                    break
            else:
                empty_lines = 0
            copied_text += line
            i += 1
        fragments.append((key_value, copied_text.strip()))
    else:
        i += 1

# === MODYFIKACJA PLIKU 2 ===
with open(file2, 'r', encoding='utf-8') as f:
    content = f.read()

for key_tag, insert_text in fragments:
    key_index = content.find(key_tag)
    if key_index == -1:
        print("error")

    # Szukamy </val> po znalezieniu <key>...</key>
    val_close_index = content.find('</val>', key_index)
    if val_close_index == -1:
        print("error")

    # Wstawiamy tekst przed </val> w tej samej linii
    content = (
        content[:val_close_index]
        + insert_text
        + content[val_close_index:]
    )

# === ZAPIS WYNIKU ===
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)
