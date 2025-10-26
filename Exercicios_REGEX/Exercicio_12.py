#Criar um ficheiro resumo.txt com os dados organizados
	#Formato por linha Exemplo:
	#Maria Gomes | 123456789 | 01/09/2025 | 1000-001 | www.exemplo.pt
import re

ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/registos.txt", "r", encoding="utf-8")
linhas = ficheiro.readlines()
ficheiro.close()

ficheiro_saida = open("resumo.txt", "w", encoding="utf-8")

for linha in linhas:

    nome_match = re.search(r'Nome:\s+([A-Za-zÀ-ÿ\s]+)\s+\|', linha)
    nif_match = re.search(r'NIF:\s+(\d{9})', linha)
    data_match = re.search(r'Data:\s+(\d{2}/\d{2}/\d{4})', linha)
    cp_match = re.search(r'Código Postal:\s+(\d{4}-\d{3})', linha)
    site_match = re.search(r'https?://([a-zA-Z0-9.-]+)', linha)

    if nome_match and nif_match and data_match and cp_match and site_match:
        nome = nome_match.group(1).strip()
        nif = nif_match.group(1)
        data = data_match.group(1)
        cp = cp_match.group(1)
        site = site_match.group(1)

        ficheiro_saida.write(f"{nome} | {nif} | {data} | {cp} | {site}\n")

ficheiro_saida.close()
print("Ficheiro 'resumo.txt' criado com sucesso!")

ficheiro = open("resumo.txt", "r", encoding="utf-8")
conteudo = ficheiro.read()
ficheiro.close()
print("\nConteúdo do ficheiro:")
print(conteudo)