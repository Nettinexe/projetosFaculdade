def contar(n1,n2):
    inicio = min(n1,n2)
    fim= max(n1,n2)

    impares = []

    for i in range(inicio, fim + 1):
        if i % 2 != 0:
            impares.append(i)

    return len(impares), impares
n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
quantidade,  lista = contar(n1,n2)
print("Essa é a quantidade de números ímpares inteiros:", quantidade)
print("Esses são os números:", lista)
    