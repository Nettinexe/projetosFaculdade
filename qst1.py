# Define uma função para somar os elementos de cada linha da matriz
def somar_linhas(matriz):
    somas = []  # Cria uma lista vazia para guardar as somas de cada linha
    for linha in matriz:  # Percorre cada linha da matriz
        soma = sum(linha)  # Soma todos os elementos da linha usando a função sum()
        somas.append(soma)  # Adiciona a soma à lista de somas
    return somas  # Retorna a lista com as somas de cada linha

# Cria uma matriz 4x4 como lista de listas vazias (4 linhas)
matriz = [[], [], [], []]

# Loop para preencher cada linha da matriz
for l in range(4):  # Vai de 0 a 3, ou seja, 4 linhas
    print(f"A seguir, escreva 4 números inteiros para adicionar à linha {l + 1}")
    for i in range(4):  # Vai de 0 a 3, preenchendo 4 colunas por linha
        valor = int(input("Digite um número: "))  # Lê um valor inteiro do usuário
        matriz[l].append(valor)  # Adiciona o valor à linha correspondente

# Exibe a matriz preenchida
print("\nMatriz digitada:")
for linha in matriz:  # Para cada linha da matriz
    print(linha)  # Exibe a linha

# Chama a função que soma as linhas e armazena o resultado em resp
resp = somar_linhas(matriz)

# Exibe a soma de cada linha
print("\nSoma de cada linha:")
for i, s in enumerate(resp):  # Percorre a lista de somas
    print(f"Linha {i + 1}: {s}")  # Exibe a soma da linha i+1
