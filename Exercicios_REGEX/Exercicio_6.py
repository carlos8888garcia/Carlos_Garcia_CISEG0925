"""#Mostra apenas os emails que terminam em .pt.
import re

ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/registos.txt", "r", encoding="utf-8")
conteudo = ficheiro.read()
ficheiro.close()

padrao = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.pt\b'
emails_pt = re.findall(padrao, conteudo, re.IGNORECASE)

print("Emails que terminam em .pt:")
for email in emails_pt:
    print(f"  - {email}")
print()"""