#Extrai todos os números de telemóvel, em qualquer dos seguintes formatos:
#•	9 dígitos juntos: 912345678
#•	Com traços: 914-567-123
#•	Com espaços: 210 987 654
import re

ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/REGEX.txt", "r", encoding="utf-8")
conteudo = ficheiro.read()
ficheiro.close()

padrao = r'\d{3}[\s-]?\d{3}[\s-]?\d{3}'
telemoveis = re.findall(padrao, conteudo)

print("Telemóveis encontrados:")
for tel in telemoveis:
    print(f"  - {tel}")
print()