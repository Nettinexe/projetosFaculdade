valores_positivos = 0
valores_negativos = 0
valor = 1
while (valor !=0):
    valor = float(input('Digite um valor ou digite 0 para encerrar o programa:'))
    if valor <0:
        valores_negativos = valores_negativos + 1
        print('Os valores negativos são:', valores_negativos)
    elif valor >0:
        valores_positivos = valores_positivos + 1
        print('Os valores positivos são:', valores_positivos)
print('Os valores negativos são:', valores_negativos)
print('Os valores positivos são:', valores_positivos)
        

        