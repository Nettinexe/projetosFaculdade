maior = 0 
menor = 0 
for i in range (1, 20):
    valor = float(input("Digite um valor:"))
    if valor >maior:
        maior = valor
    elif valor <menor:
        menor = valor
print("Maior valor e:", maior)
print("Menor valor e:", menor)            