# Funções:
# Interative help
# -> Para entrar na ajuda interativa do python, basta estar no console e digitar help() e depois digitar a função ou lib que deseja consultar.
# ou
help(print) # ou
print(input.__doc__)

# docstring
# É uma string de documentação
def retiraNull(list):
    """
    A função retiraNull, faz com que se retire todas as strings de conteudo
    'null' e substitua por 'NULO'.
    Essa função recebe como parametro uma lista.
    """
    for i, nome in enumerate(list):
        if nome == 'null':
            list[i] = 'NULO'
    return list

print(help(retiraNull))

# Parâmetros opcionais

def soma(a, b, c=0): # O parametro =0 significa que se caso c não for preenchido, receberá 0 por defaut.
    s = a + b + c
    print(s)

# Escopo de variáveis
# uma variável declarada dentro de uma função, não existirá fora de seu escopo.
# para modificar o conteudo de uma variável global dentro de uma função faz-se
c = 0
def soma2(a, b):
    global c
    c = 5
    d = a + b
    return d
soma2(5,2)
print(c)