cargo = input("Digite seu cargo:")
tempo = int(input("Digite o tempo de contribuição:"))
if cargo == "Programador" and tempo <2:
    print("Seu percentual é 2%")
elif cargo == "Programador" and tempo >=2:
    print("Seu percentual é 3%")
elif cargo == "Analista" and tempo <3:
    print("Seu percentual é 4%")
elif cargo == "Analista" and tempo >=3:
    print("Seu percentual é 5%")
elif cargo == "Gerente" and tempo <=4:
    print("Seu percentual é 6%")
elif cargo == "Gerente" and tempo >4:
    print("Seu percentual é 7%")