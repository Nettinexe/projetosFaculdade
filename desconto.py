valor = 0
produto = float(input("Digite um valor ou digite 0 para encerrar:"))
while produto !=0:
    soma = produto + valor
    valor=soma
    print("Valor da compra é R$:",valor)
    if valor >=100:
        desconto=valor * 0.10
        print("Seu desconto e R$ :",desconto)
        valor_final= valor - desconto
        print("valor final é R$:",valor_final)
    produto = float(input("Digite um valor ou digite 0 para encerrar:"))