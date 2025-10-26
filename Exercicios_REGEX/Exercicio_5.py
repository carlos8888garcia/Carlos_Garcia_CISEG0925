#Cria um ficheiro chamado extraidos.txt com a seguinte estrutura por linha:
#•	Ana Costa | ana.costa@gmail.com | 912345678
#•	João Silva | joao_silva@empresa.pt | 914-567-123
import re

ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/REGEX.txt", "r", encoding="utf-8")
linhas = ficheiro.readlines()
ficheiro.close()

ficheiro_saida = open("extraidos.txt", "w", encoding="utf-8")

for linha in linhas:

    nome_match = re.search(r'Nome:\s+([A-Za-zÀ-ÿ\s]+),', linha)

    email_match = re.search(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', linha)

    tel_match = re.search(r'\d{3}[\s-]?\d{3}[\s-]?\d{3}', linha)

    if nome_match and email_match and tel_match:
        nome = nome_match.group(1).strip()
        email = email_match.group(0)
        tel = tel_match.group(0)

        ficheiro_saida.write(f"{nome} | {email} | {tel}\n")

ficheiro_saida.close()
print("Ficheiro 'extraidos.txt' criado com sucesso!")

ficheiro = open("extraidos.txt", "r", encoding="utf-8")
conteudo = ficheiro.read()
ficheiro.close()
print("\nConteúdo do ficheiro:")
print(conteudo)