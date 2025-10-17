# Define uma função que soma os valores de cada coluna da matriz
def somar_colunas(matriz):
    somas = [0] * 4  # Cria uma lista com 4 zeros, um para cada coluna
    for linha in matriz:  # Percorre cada linha da matriz
        for i in range(4):  # Para cada índice de coluna
            somas[i] += linha[i]  # Soma o valor da posição i da linha
    return somas  # Retorna a lista com as somas das colunas

# Cria a estrutura da matriz com 4 linhas vazias
matriz = [[], [], [], []]

# Preenche a matriz com dados do usuário
for l in range(4):  # Para cada linha
    print(f"A seguir, escreva 4 números inteiros para adicionar à linha {l + 1}")
    for i in range(4):  # Para cada coluna
        valor = int(input("Digite um número: "))  # Lê um número inteiro
        matriz[l].append(valor)  # Adiciona o número à linha correspondente

# Exibe a matriz preenchida
print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

# Chama a função que soma as colunas
resp = somar_colunas(matriz)

# Exibe a soma de cada coluna
print("\nSoma de cada coluna:")
for i, s in enumerate(resp):
    print(f"Coluna {i + 1}: {s}")
