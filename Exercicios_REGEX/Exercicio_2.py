#Extrai e imprime todos os endereços de email encontrados no ficheiro.
import re

ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/REGEX.txt", "r", encoding="utf-8")
conteudo = ficheiro.read()
ficheiro.close()

padrao = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(padrao, conteudo)

print("Emails encontrados:")
for email in emails:
    print(f"  - {email}")
print()