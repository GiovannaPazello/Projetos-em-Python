'''Gere uma lista de 30 números aleatórios entre 1 e 100. Não pode haver número repetido na lista.'''

from random import randint
lista = []
for i in range(30):
    nrogerado = randint(0,100)
    if nrogerado not in lista:
        lista.append(nrogerado)
print(lista)