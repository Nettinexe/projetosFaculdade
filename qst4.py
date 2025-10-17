# Cria uma matriz com 8 listas vazias, uma para cada aluno
matriz = [[], [], [], [], [], [], [], []]

# Coleta o nome e 3 notas de cada aluno
for i in range(8):  # Loop para 8 alunos
    nome = input(f"Digite o nome do {i + 1}º aluno: ")  # Solicita o nome do aluno
    matriz[i].append(nome)  # Adiciona o nome à linha correspondente

    for k in range(3):  # Loop para as 3 notas
        nota = int(input(f"Digite a nota {k + 1} do aluno: "))  # Solicita a nota
        matriz[i].append(nota)  # Adiciona a nota à mesma linha

# Exibe a matriz com nomes e notas
print("\nDados dos alunos:")
for aluno in matriz:  # Para cada linha da matriz
    print(aluno)  # Exibe nome e notas do aluno
