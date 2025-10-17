# Define uma função que multiplica todos os elementos da matriz pelo valor da posição [0][0]
def mult_matriz(matriz):
    multiplicador = matriz[0][0]  # Pega o valor da posição [0][0] da matriz
    nova_matriz = []  # Cria uma nova matriz (vazia) para guardar os resultados

    for linha in matriz:  # Percorre cada linha da matriz original
        nova_linha = []  # Lista para guardar a linha multiplicada
        for elemento in linha:  # Percorre cada elemento da linha
            nova_linha.append(elemento * multiplicador)  # Multiplica e adiciona à nova linha
        nova_matriz.append(nova_linha)  # Adiciona a linha já processada à nova matriz

    return nova_matriz  # Retorna a nova matriz com os valores multiplicados

# Cria uma matriz com 3 linhas vazias (será 3x4)
matriz = [[], [], []]

# Preenche a matriz com números fornecidos pelo usuário
for j in range(3):  # Para cada linha
    print(f"Iniciando processo de inserção de dados na linha {j + 1}:")
    for k in range(4):  # Para cada coluna
        valor = int(input("Digite um número inteiro: "))  # Lê um número inteiro
        matriz[j].append(valor)  # Adiciona o valor à linha correspondente

# Exibe a matriz original
print("\nMatriz original:")
for linha in matriz:
    print(linha)

# Chama a função que multiplica todos os elementos
resp = mult_matriz(matriz)

# Exibe a matriz resultante da multiplicação
print("\nMatriz após multiplicação pelo elemento [0][0]:")
for linha in resp:
    print(linha)
