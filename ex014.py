# Funções:
# Para criar uma função, basta colocar a palavra def no início e no final do nome da função abrir e fechar parêntese.
# Os parâmetros podem ser passados dentro do parêntese.
def titulo(title):
    print('-' * 30)
    print(f'{title}')
    print('-' * 30)

titulo('Funções em python')

# Exemplo função de soma:

def soma(a, b):
    s = a + b
    print(s)
soma(5,20) # Retorna 25. É obrigatório passar os dois parâmentos.

# Empacotamento:
# Significa que pode-se alimentar mais valores como entrada de uma fanção.]
def numerosN(*num): # -> cria-se um tupla
    tam = len(num)
    print(f'Recebi {tam} valores como parametro.')
    print(f'Eles são {num}')
numerosN(5,6,8,5,6,2,6,8)
numerosN(1,4,8,2,7,5)

def somaN(*num):
    soma = 0
    for n in num:
        soma += n
    print(soma)

somaN(5,6,4)

# para especificar o retorno de uma função, basta na ultima linha especificar seu retorno
def som(*n):
    total = 0
    for item in n:
        total += item
    return total # -> Vai retornar o resultado de todas as subtrações

print(som(5,4))

