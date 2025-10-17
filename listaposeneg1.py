def filtrar_positivos(n1,n2,n3,n4,n5):
    positivos = []  # lista para armazenar os positivos
    if n1 > 0:
        positivos.append(n1)
    if n2 > 0:
        positivos.append(n2)
    if n3 > 0:
        positivos.append(n3)
    if n4 > 0:
        positivos.append(n4)
    if n5 > 0:
        positivos.append(n5)    
    return positivos
n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
n3 = int(input("Digite um número:"))
n4 = int(input("Digite um número:"))
n5 = int(input("Digite um número:"))

resultado = filtrar_positivos(n1,n2,n3,n4,n5)
print("Esses são os números positivos digitados:",resultado)  

