#Extrair apenas os domínios dos sites
	#Exemplo: www.exemplo.pt, empresa.com, escola.edu
import re

ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/registos.txt", "r", encoding="utf-8")
conteudo = ficheiro.read()
ficheiro.close()

padrao = r'https?://([a-zA-Z0-9.-]+)'
dominios = re.findall(padrao, conteudo)

print("Domínios encontrados:")
for dominio in dominios:
    print(f"  - {dominio}")
print()