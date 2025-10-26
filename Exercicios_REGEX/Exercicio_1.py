#Lê o conteúdo do ficheiro e imprime-o no ecrã
ficheiro = open("E:/Atec/Carlos_Garcia_CISEG0925/Exercicios_REGEX/REGEX.txt", "r", encoding="utf-8")
conteudo = ficheiro.read()
ficheiro.close()

print(conteudo)
print()