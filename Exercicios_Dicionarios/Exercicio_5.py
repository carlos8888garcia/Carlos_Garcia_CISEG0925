#Pede ao utilizador que introduza uma palavra.
#Em seguida, cria um dicionário onde cada letra da palavra é uma chave e o seu valor é o número de vezes que essa letra aparece.
#Exemplo de entrada: "banana"
#Resultado esperado: {'b': 1, 'a': 3, 'n': 2}
# Saída: {'b': 1, 'a': 3, 'n': 2}


palavra = input("Intoduza uma palavra :")
letras={}


for i in palavra:
    if i in letras:
        letras[i] += 1
    else:
        letras[i] = 1
print(letras)