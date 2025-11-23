maior = 0 
menor = 0 
meio1 = 0
meio2 = 0
for i in range(1,5):
    numero = int(input("Digite um numero:"))
    if i == 1:
        menor = numero
        maior = numero
        meio1 = numero 
        meio2 = numero
    if numero > maior:
        maior=numero
    if menor < menor:
        menor = numero
    if numero > menor and numero < maior:
        numero = meio1
    if numero > meio1 and numero < maior:
        numero = meio2
print("A ordem crescente dos numeros é:",menor,meio1,meio2,maior)
