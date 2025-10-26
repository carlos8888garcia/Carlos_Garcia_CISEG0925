#Dado os seguintes dicionários:
#d1 = {'a': 1, 'b': 2}
#d2 = {'c': 3, 'd': 4}
#Cria um novo dicionário que contenha os pares chave-valor dos dois dicionários juntos.

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3= {**d1,**d2}

print(d3)


