#Extrair datas no formato DD/MM/AAAA
import re

ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/registos.txt", "r", encoding="utf-8")
conteudo = ficheiro.read()
ficheiro.close()

padrao = r'\d{2}/\d{2}/\d{4}'
datas = re.findall(padrao, conteudo)

print("Datas encontradas:")
for data in datas:
    print(f"  - {data}")
print()