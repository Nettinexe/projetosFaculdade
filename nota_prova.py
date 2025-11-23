def conceito(d,c,b,a):
    if valor >= 0 and  valor <=49:
        return "D"
    elif valor >=50 and valor <=69:
        return "C"
    elif valor >=70 and valor <=89:
        return "B"
    elif valor >=90 and valor <=100:
        return "A"
    
valor = float(input("Digite sua média:"))
resultado = conceito(valor, valor, valor ,valor)
print("Seu conceito é", resultado)


