def idade_dias(a,m,d):
    dias_anos = anos * 365
    dias_meses = meses * 30
    resultado = dias_anos + dias_meses +  dias
    return resultado
anos = int(input("Digite quantos anos?"))
meses = int(input("Digite quantos meses?"))
dias = int(input("Digite quantos dias?"))
resultado = idade_dias(anos,meses,dias)
print("Idade em dias", resultado)







