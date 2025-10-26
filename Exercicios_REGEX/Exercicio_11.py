#Validar se todos os NIFs começam com um dígito válido
	#Em Portugal, os NIFs geralmente começam com: 1, 2, 3, 5, 6 ou 8.
import re

ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/registos.txt", "r", encoding="utf-8")
conteudo = ficheiro.read()
ficheiro.close()

padrao = r'NIF:\s+(\d{9})'
nifs = re.findall(padrao, conteudo)

digitos_validos = ['1', '2', '3', '5', '6', '8']

print("Validação de NIFs:")
for nif in nifs:
    primeiro_digito = nif[0]
    if primeiro_digito in digitos_validos:
        print(f"{nif} - Válido")
    else:
        print(f"{nif} - Inválido")
print()