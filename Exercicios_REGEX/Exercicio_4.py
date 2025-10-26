#Extrai todos os nomes completos após a palavra "Nome: ".
import re

ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/REGEX.txt", "r", encoding="utf-8")
conteudo = ficheiro.read()
ficheiro.close()

padrao = r'Nome:\s+([A-Za-zÀ-ÿ\s]+),'
nomes = re.findall(padrao, conteudo)

print("Nomes encontrados:")
for nome in nomes:
    print(f"  - {nome}")
print()