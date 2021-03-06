# Estruturas condicionais
a = 15
b = 10
# bloco
if a < b:
    print(a)
else:
    print(b)

# linha
print("Linha")

print("{} é maior".format(a) if (a > b) else "{} é maior".format(b))