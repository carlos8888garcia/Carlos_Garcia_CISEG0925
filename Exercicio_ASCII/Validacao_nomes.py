def comparar_nomes(nome1, nome2):
    """
    Compara dois nomes caractere a caractere usando valores ASCII.
    Retorna:
    -1 se nome1 vem antes de nome2
     1 se nome1 vem depois de nome2
     0 se são iguais
    """
    tamanho_minimo = min(len(nome1), len(nome2))
    
    for i in range(tamanho_minimo):
        valor_ascii1 = ord(nome1[i])
        valor_ascii2 = ord(nome2[i])
        
        if valor_ascii1 < valor_ascii2:
            return -1
        elif valor_ascii1 > valor_ascii2:
            return 1
    if len(nome1) < len(nome2):
        return -1
    elif len(nome1) > len(nome2):
        return 1
    else:
        return 0

def ordenar_nomes(nomes):
    lista_ordenada = nomes.copy()
    n = len(lista_ordenada)
    
    # Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compara os nomes
            if comparar_nomes(lista_ordenada[j], lista_ordenada[j + 1]) > 0:
                # Troca de posição
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    
    return lista_ordenada
nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade"
]

print("Lista original:")
for nome in nomes:
    print(f"  {nome}")

print("\n--- A ordenar... ---\n")

nomes_ordenados = ordenar_nomes(nomes)

print("Lista ordenada alfabeticamente:")
for nome in nomes_ordenados:
    print(f"  {nome}")

print("\n--- Valores ASCII dos primeiros caracteres ---")
for nome in nomes_ordenados:
    primeira_letra = nome[0]
    print(f"  {nome} → '{primeira_letra}' = ASCII {ord(primeira_letra)}")
