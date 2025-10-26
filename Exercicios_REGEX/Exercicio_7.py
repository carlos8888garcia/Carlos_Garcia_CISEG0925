#Extrair todos os NIFs (9 dígitos)
import re

ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/registos.txt", "r", encoding="utf-8")
conteudo = ficheiro.read()
ficheiro.close()

padrao = r'NIF:\s+(\d{9})'
nifs = re.findall(padrao, conteudo)

print("NIFs encontrados:")
for nif in nifs:
    print(f"  - {nif}")
print()