## Tuplas
# As tuplas são imutáveis.
from time import sleep
lanche = ('Hambúrguer', 'Suco', 'Pudim', 'Pizza')

for item in lanche:
    print(f'agora estou comento um {item}')
    sleep(1.5)
print('Finish')
