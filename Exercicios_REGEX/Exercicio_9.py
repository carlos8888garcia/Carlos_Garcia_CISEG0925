#Extrair códigos postais portugueses (1234-567)
import re

ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/registos.txt", "r", encoding="utf-8")
conteudo = ficheiro.read()
ficheiro.close()

padrao = r'\d{4}-\d{3}'
codigos = re.findall(padrao, conteudo)

print("Códigos postais encontrados:")
for codigo in codigos:
    print(f"  - {codigo}")
print()