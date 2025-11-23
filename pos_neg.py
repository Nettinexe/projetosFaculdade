positivos = 0 
negativos = 0
for i in range (1, 10):
    valor = float(input("Digite um valor:"))
    if valor >0:
        positivos += 1
    else:
        negativos += 1
print("os valores positivos sao:", positivos)
print("os valores negativos sao:", negativos)
            

