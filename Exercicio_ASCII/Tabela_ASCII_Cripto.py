def calcular_chave(chave):
    """Soma os valores ASCII de cada letra da chave."""
    soma = 0
    for letra in chave:
        soma += ord(letra)
    return soma

def criptografar(mensagem, chave):
    """Criptografa a mensagem."""
    if chave == "":
        print("Erro: A chave não pode ser vazia!")
        return None
    
    chave_numerica = calcular_chave(chave)
    codigos = []
    
    for letra in mensagem:
        codigo_original = ord(letra)
        
        if 32 <= codigo_original <= 126:

            novo_codigo = codigo_original - 32
            novo_codigo = (novo_codigo + chave_numerica) % 95
            novo_codigo = novo_codigo + 32
        else:
            novo_codigo = codigo_original + chave_numerica
        
        codigos.append(novo_codigo)
    
    return codigos

def descriptografar(codigos, chave):
    """Descriptografa os códigos."""
    if chave == "":
        print("Erro: A chave não pode ser vazia!")
        return None
    
    chave_numerica = calcular_chave(chave)
    mensagem = ""
    
    for codigo in codigos:
        if 32 <= codigo <= 126:
            codigo_original = codigo - 32
            codigo_original = (codigo_original - chave_numerica) % 95
            codigo_original = codigo_original + 32
        else:
            codigo_original = codigo - chave_numerica
        
        mensagem += chr(codigo_original)
    
    return mensagem

def listar(codigos):
    """Mostra os códigos criptografados."""
    print("\nMensagem criptografada:")
    print(codigos)

print("=== CRIPTOGRAFIA ASCII ===\n")

while True:
    print("\n1. Criptografar")
    print("2. Descriptografar")
    print("3. Sair")
    
    opcao = input("\nEscolha: ")
    
    if opcao == "1":
        mensagem = input("\nMensagem: ")
        chave = input("Chave: ")
        
        resultado = criptografar(mensagem, chave)
        
        if resultado != None:
            valor_chave = calcular_chave(chave)
            print(f"\nChave numérica: {valor_chave}")
            listar(resultado)
    
    elif opcao == "2":
        entrada = input("\nCódigos (separados por vírgula): ")
        chave = input("Chave: ")
        
        codigos = []
        numeros = entrada.split(',')
        for numero in numeros:
            codigos.append(int(numero))
        
        resultado = descriptografar(codigos, chave)
        
        if resultado != None:
            print(f"\nMensagem original: {resultado}")
    
    elif opcao == "3":
        print("\nAté breve!")
        break
    
    else:
        print("\nOpção inválida!")
