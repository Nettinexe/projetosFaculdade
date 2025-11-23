resultado = 1

valor = int(input("Digite um valor:"))
if valor > 0:
    for i in range (1, valor + 1):
        resultado *= i
    print(resultado)
else:
    print("Valor inválido")