maior = 0
menor = 1
valor = 2
contador = 0
while contador <20:
    valor = float(input('Digite um valor:'))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    contador += 1
print('O menor valor é:', menor, "e o maior valor é:", maior)