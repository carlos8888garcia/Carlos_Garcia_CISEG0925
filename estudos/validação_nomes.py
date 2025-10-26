import time
i = 0
flag_espaco = False

nome = str(input("Digite o seu nome completo :"))

while i < len(nome):
    if i == 0:
        if ord(nome[i]) >= 65 and ord(nome[i]) <=90:
            print("Válido") 
        else:
            print("Inválido")   
       
    elif ord(nome[i]) == 32:
        if ord(nome[i+1]) >= 65 and ord(nome[i+1]) <=90:
            print("Válido")
        else:
            print("Inválido")
    else:
        if ord(nome[i]) >= 97 and ord(nome[i]) <=122: 
            print("válido") 
        else:
            print("inválido")          
    i=i+1