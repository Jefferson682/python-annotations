# Estruturas
# Condições aninhadas
varA = 15
varB = 15
varC = 11

if varA > varB:
    if varB > varC:
        print("O menor é o varC")
    elif varB == varC and varA > varB:
        print("varB e varC são iguais")
    else:
        print("O menor é o varB")
elif varB > varA:
    if varA > varC:
        print("O menor é o varC")
    elif varA == varC and varB > varA:
        print("varA e varC são iguais")
    else:
        print("O menor é o varA")
elif varC > varA:
    if varA > varB:
        print("O menor é varB")
    elif varA == varB and varC > varA:
        print("varA e varB são iguais")
    else:
        print("O menor é varA")
elif varA == varB == varC:
    print("são todos iguais")
else:
    print("\033[0;33;44m Nunca vai chegar aqui! \033[m") #chegou várias vezes
