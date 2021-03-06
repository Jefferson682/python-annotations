# Listas
# Listas são mutáveis:
frutas = ['banana', 'mamão', 'laranja']
print(frutas)

# Adicionar elementos:
frutas.append('abacate')
print(frutas)

# Adicionar em posição especifica
frutas.insert(0,'acerola') # Acidiona acerola no indice 0

# Percorrer elementos:
for fruta in frutas:
    print(f'Você tem a fruta: {fruta}')
print('Fim da lista')

# Remover elementos:
frutas.remove('banana')
print(frutas)

# Remover se houver na lista
if 'banana' in frutas:
    frutas.remove('banana')
else:
    print('Não tem banana')

# Remover ultimo elemento:
frutas.pop() # Ou frutas.pop(INDICE) -> indice específico
print(frutas)

# Para saber o tamanho de uma lista utilizasse o método len()
print(len(frutas))

# Colocar em ordem as frutas
frutas.sort()
print(frutas)

# colocar em ordem os numeros
numeros = [1,2,3,4,8,5,6,9,7]
numeros.sort()
print(numeros)

# colocando em ordem inversa
numeros.sort(reverse=True) # também pode ser para Strings
print(numeros)

# Listas dentro de listas:
lista = [['José', 18],['Antônio', 50],['João', 15],['Maria', 19],['José', 19]]
print(lista)
# Imprimindo um item da lista
print(lista[1])
# Imprimindo um item da lista interna a outra lista
print(lista[0][0]) # -> É pra ser José

# imprimindo todos os itens da lista interna na posição 1: antônio 50
for dados in lista[1]:
    print(f'{dados}')

# trocando dados da lista interna
for pessoas in lista:
    if pessoas[0] == 'José':
        pessoas[0] = 'Novo Nome'
print(lista)


