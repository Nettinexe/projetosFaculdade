def contagem_n(numeros):
    contador_negativo = 0
    for i in range(len(numeros)):
        if numeros[i] < 0:
            contador_negativo = contador_negativo + 1
    return contador_negativo
def contagem_p(numeros):
    contador_positivo = 0
    for i in range(len(numeros)):
        if numeros[i] > 0:
            contador_positivo = contador_positivo + 1
    return contador_positivo
def media_n(numeros):
    media_n = 0
    for i in range(len(numeros)):
        soma_valor += numeros
        media_n = soma_valor / 10
    return media_n 
        
    


numeros = []

for i in range(10):
    num = int(input("Digite um valor:"))
    numeros.append(num)

print(f"Existem {(contagem_n(numeros))} números negativos")
print(f"Existem {(contagem_p(numeros))} números positivos")
print(f"A média dos números é {(media_n(numeros))}")