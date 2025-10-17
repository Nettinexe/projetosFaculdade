resultado = 1
chances = int(input("Digite quantos valores serao digitados:"))
for i in range(1,chances + 1):
    numero = int(input("Digite um valor:"))
    resultado = 1
    for x in range (1, numero + 1):
        resultado *= x
        print(x)
    print(resultado)
