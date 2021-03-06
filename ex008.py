#Laços de repetição for
for c in range(0,10):
    print("Esse é o laço {}".format(c + 1))
print("Fim do laço")

#Laço de repetição for decrescente:
for c in range(10, 0, -1):
    print("Esse é o laço {}".format(c - 1))
print("Fim do laço")

#Laço de repetição for com pulos:
for c in range(0, 10, 2):
    print("Esse é o laço {}".format(c + 1))
print("Fim do laço")

#Laço de repetição for com biblioteca de time
from time import sleep
for c in range(10, 0, -1):
    print("Contagem com {} segundo".format(c))
    sleep(1.0)

# Por defaut o final de cada loop existe uma quebra de linha. pode ser resolvido com um end

for c in range(1,5,1):
    print("{}".format(c), end=' ')