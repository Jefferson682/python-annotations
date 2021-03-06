# -> Comentários em python3 é com # no início

# Em python tudo é objeto.
# O objeto String é imutável por meios de métodos.

# Declaração de variáreis
# Para declarar variáveis em python, não é necessário declarar seu tipo.
# A tipagem é dinâmica.
inteiro = 11
texto = "String"
real = 1.5
boleano = True #Bolean sempre com primeira letra maiúscula.

# print
print('Hello World')
# print com variável
print('string {}'.format(texto))
print('string {}, int {}'.format(texto, inteiro))

# ver tipo de variável -> Função type()
print(type(texto))

# teste de conteudo string:
print(texto.isalnum())

# Insersão de dados com função input:
nome = input('Qual o seu nome:')

# Insersão com tipos primitivos:
# Os tipos primitivos são: int, float, bool, str.
n1 = int(input("Digite um número"))

# Operadores aritméticos:
x + x = 0    # Adição
x - x = 0    # Subtração
x * x = 0    # Multiplicação
x / x = 0    # Divisão
x ** x = 0   # Potência
x // x = 0   # Divisão inteira
x % x = 0    # Resto da divisão

# importando módulos -> bibliotecas
# biblioteca inteira
import {nome da biblioteca}
# importar método específico de uma biblioteca
from {biblioteca} import {método}

#Exemplo
import math
from math import floor # ou
from math import floor, ceil # mais de um método.

# Exemplo de uso:
a = 5
x = math.sqrt(a) # Calcula a raiz de -> a

# Manipulação de string
nome = "Jefferson"
# cada caractere de uma string seria como uma posição numa lista.
print(nome[5])
print(nome[0:5])
# Análise de string
# mostrar quantidade de caracteres:
nome = "Jefferson"
print(len(nome))
# contar quantas vezes um caractere aparece:
print(nome.count('o'))
# buscar caractere -> mostra onde começa 
print(nome.find('fer'))
# se não existir retorna -1
print(nome.find('y'))
# Subistituição de string
print(nome.replace("Jefferson", "João")) # Pórem, não troca permanentemente o valor de nome.
print(nome)
# Deixar maiusculo
print(nome.upper()) # Pórem, não troca permanentemente o valor de nome.
print(nome)
# deixar menusculo
print(nome.lower()) #  Pórem, não troca permanentemente o valor de nome.
# deixar primeira letra da fraze em maiusculo
frase = "esta é uma frase"
print(frase.capitalize())
# deixar primeira letra de todas as palavras em upper
print(frase.title())
# Retirar espaços inúteis das strings
frase.strip()
# Dividir string
dividido = frase.split()
print(dividido)
# Juntar strings
junto = '-'.join(dividido) # O que estar entre aspas é o reparador e pode ser um espaço vazio também.
print(junto)
# Bloco de texto
blocoTexto = """
Este é
um bloco de 
texto
"""
print(blocoTexto)

# Estruturas condicionais
if (condição):
    (executa esse bloco)
else:
    (acontece isso)
# Exemplo:
a = 15
b = 10
if a < b:
    print(a)
else:
    print(b)

# Estrutura em linha
(faça isso) if (condição) else (faça aquilo)
# Exemplo
print("{} é maior".format(a) if (a > b) else "{} é maior".format(b))

# Trabalhando com datas
from datetime import date
ano = date.today().year
print(ano)

# cores no terminal -> padrão ASCI
print('\033[0;33;44m Olá mundo \033[m')

# Laços de repetição for
for c in range(0,10):
    print("Esse é o laço {}".format(c + 1))
print("Fim do laço")

# Laço de repetição for decrescente:
for c in range(10, 0, -1):
    print("Esse é o laço {}".format(c - 1))
print("Fim do laço")

# Laço de repetição for com pulos:
for c in range(0, 10, 2):
    print("Esse é o laço {}".format(c + 1))
print("Fim do laço")

# Biblioteca de tempo -> SLEEP
from time import sleep

# Laço de repetição for com biblioteca de time
from time import sleep
for c in range(10, 0, -1):
    print("Contagem com {} segundo".format(c))
    sleep(1.0)
