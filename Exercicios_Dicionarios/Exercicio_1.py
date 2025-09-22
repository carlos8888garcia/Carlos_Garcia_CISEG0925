# Cria um dicionário chamado alunos que receba nome, idade e curso de cada aluno:
# 1- Inserir
# 2- Listar
# O mesmo deve imprimir cada elemento do dicionário no seguinte formato por cada aluno:
# Exemplo:
# nome: Maria
# idade: 20
# curso: Engenharia

Alunos = {"Nome" :[], "Idade" :[], "Curso" :[] }


def inserir():

    Alunos["Nome"].append(input("Digite o seu nome :"))
    Alunos["Idade"].append(input("Digite a sua idade :"))
    Alunos["Curso"].append(input("Digite o seu curso :"))


def menu():
    
    while True:
        
        print("|------Menu------|")

        print("1-Inserir")

        print("2-Listar")
        print("|----------------|")

        escolha = input("O que deseja fazer? :")

        if escolha == '1':
            inserir()

        if escolha == '2':
            for i in range (len(Alunos["Nome"])):
                print(f"{"Nome"} :{Alunos["Nome"][i]} \n")
                print(f"{"Idade"} :{Alunos["Idade"][i]} \n")
                print(f"{"Curso"} :{Alunos["Curso"][i]} \n")
                print("-----------------")
        else:
            print("Opção invalida!")

menu()

