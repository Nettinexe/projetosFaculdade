soma_salarios = 0
pesquisados = 10
maior_salario =0
menor_que_100 = 0 
salario = float(input("Digite seu salario ou digite 0 para encerrar:"))
for i in range (1,11,1):
    salario = float(input("Digite seu salario ou digite 0 para encerrar:"))
    soma_salarios +=salario
    if salario >maior_salario:
        maior_salario = salario
    elif salario <= 100:
        menor_que_100 +=1
        percentual = menor_que_100 / pesquisados * 100
    elif salario == 0 :
         break
media_salarial = soma_salarios / pesquisados
print("a media salarial da populaçao e:",media_salarial)
print("o maior salario e:",maior_salario)
print(percentual,"%")

soma_filhos = 0 
filhos = float(input("Digite o numero de filhos ou digite um número negativo para encerrar:"))
for i in range (1,11,1):
    filhos = float(input("Digite o numero de filhos ou digite um número negativo para encerrar:"))
    soma_filhos +=filhos
    if filhos <0:
         break
media_filhos = soma_filhos / pesquisados
print("a media de filhos da populaçao e:",media_filhos)


