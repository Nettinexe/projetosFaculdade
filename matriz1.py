'''
matriz = [[],[],[]]
for i in range(0,3):
    for j in range(0,2):
        valor = int(input("Digite um valor:"))
        matriz[i].append(valor)
# print("Matriz:", matriz)
for j in range(0,2):
    print("")
    for i in range(0,3):
        print( matriz[i][j],'',end='')
'''
mat = []
n = 0
linhas = int(input("Quantas linhas você quer?:"))
num = int(input("Quantos números você quer em cada linha?:"))
for i in range(linhas):
    linha = []
    for i in range(num):
        n = n + 1
        linha.append(n)
    mat.append(linha)
print("Matriz:", mat)
