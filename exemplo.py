descricao = ['null', 'descrição qualquer','null', 'descrição qualquer','null', 'descrição qualquer','null', 'descrição qualquer']
numero = ['000.00.00000.00000','000.00.00000.00000','000.00.00000.00000','000.00.00000.00000','000.00.00000.00000','000.00.00000.00000','000.00.00000.00000','000.00.00000.00000']
tipo = ['Manual','Manual','Manual','Manual','Manual','Manual','Manual','Manual']
data = ['2020','2020','2020','2020','2020','2020','2020','2020']
df = {}
df['descricao'] = descricao
df['numero'] = numero
df['tipo'] = tipo
df['data'] = data

# print(df)

for pos, descricao in enumerate(df['descricao']):
    if descricao == 'null':
         df['descricao'][pos] = 'Sem descricao'

print(df)