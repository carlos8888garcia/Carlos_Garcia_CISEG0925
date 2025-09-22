#1.	Adiciona os seguintes pares chave-valor:
#	nome: "Telemóvel"
#	preço: 1500
#	stock: 30
#	Remove a chave stock do dicionário.
#	Imprime o dicionário final

produto = {}

produto["nome"]= {"Telemóvel"}
produto["preco"]= {"1500 "}
produto["stock"]= {"30 "}

del produto["stock"]

print(produto)