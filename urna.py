soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
nulo = 0
branco = 0
for i in range (1, 11):
  pepe = int(input(" Coloque o numero de voto do seu candidato:"))
  if pepe == 1:
    soma1 += 1
    print("Bolsonaro JAIR")
  elif pepe == 2:
    soma2 += 1
    print("Dilma")
  elif pepe == 3:
    soma3 += 1
    print("Felipe Neto")
  elif pepe == 4:
     soma4 += 1
     print("Eneas")
  elif pepe == 5:
     print("nulo")
     nulo += 1
  elif pepe == 6:
        print("branco")
        branco += 1
print("bolsonaro",soma1)
print("dilma",soma2)
print("felipe neto",soma3)
print("eneas",soma4)
print("nulo",nulo)
print("branco",branco)
