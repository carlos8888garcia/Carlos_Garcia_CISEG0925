#Encontrar registos com datas anteriores a 2025
#•	Usar datetime em conjunto com regex.
import re
from datetime import datetime

ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/registos.txt", "r", encoding="utf-8")
linhas = ficheiro.readlines()
ficheiro.close()

print("Registos com datas anteriores a 2025:")

for linha in linhas:

    nome_match = re.search(r'Nome:\s+([A-Za-zÀ-ÿ\s]+)\s+\|', linha)
    data_match = re.search(r'Data:\s+(\d{2}/\d{2}/\d{4})', linha)

    if nome_match and data_match:
        nome = nome_match.group(1).strip()
        data_str = data_match.group(1)

        data_obj = datetime.strptime(data_str, "%d/%m/%Y")

        if data_obj.year < 2025:
            print(f"  - {nome}: {data_str} (Ano {data_obj.year})")
print()