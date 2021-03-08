# Dicionários:

dados = {
    'Nome':'Jefferson',
    'Sobrenome':'Nascimento',
    'idade':15
}

for dado in dados:
    print(dados[dado])

print(dados) # Imprime tudo
print(dados.items()) # Pega chave valor
print(dados.values()) # Imprime os valores
print(dados.keys()) # Imprime os índices

dados2 = {
    'Nome':'Maria',
    'Sobrenome':'Ana',
    'idade':20
}

# Lista com dicionários dentro
pessoas = list()
pessoas.append(dados)
pessoas.append(dados2)

print(pessoas)

# Acessar primeira pessoa
print(pessoas[0])
# Acessar nome da primeira pessoa
print(pessoas[0]['Nome'])

# Acessar todas as idades
for pessoa in pessoas:
    print(pessoa['idade'])

# Mudando valores de dicionarios:
print(pessoas)
for pessoa in pessoas:
    if pessoa['Nome'] == 'Jefferson':
        pessoa['Nome'] = 'João'
    else:
        pass
print(pessoas)

# Imprimindo chave valor
for k, v in dados.items():
    print(f'{k} = {v}')

print('-------------------------')

for pessoa in pessoas:
    print('Pessoa:')
    for k, v in pessoa.items():
        print(f'{k} = {v}')
    