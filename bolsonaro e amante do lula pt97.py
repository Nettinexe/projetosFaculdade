chico = 150
ze = 130
for i in range(1, 51, 1):
    chico += 2
    ze += 3
    if ze > chico:
        print("Ze tem  essa altura", ze,"Chico tem essa altura", chico)
        break
    print("Passaram-se",i,"anos")
    
