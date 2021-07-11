'''Faça um programa que gere números aleatórios entre 5 e 95 até gerar um número divisível por 7.
Quando isso ocorrer informar:

- a quantidade de números divisíveis por 4 e maiores que 30 que foram gerados

- a quantidade de números pares OU menores que 30 que foram gerados.

- o percentual de números pares e o percentual de números impares

- o percentual de números ímpares dentre os números gerados que eram menores que 60

- o maior número par gerado

- o menor número impar gerado'''

import random
cont = 0
lista = []
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0

for i in range(100):
    x = random.randint(5,20)
    lista.append(x)
    if x%7 == 0:
        if len(lista)%4 == 0 and len(lista) > 30:
            cont1 +=1
        if len(lista)%2 == 0 and len(lista) <30:
            cont2 +=1
        if len(lista)%2 == 0:
            cont3 +=1
        if len(lista)%2 != 0:
            cont4 += 1
            if len(lista) < 60:
                cont5 +=1

print('a quantidade de números divisíveis por 4 e maiores que 30 que foram gerados é {}'.format(cont1))
print('a quantidade de números pares OU menores que 30 que foram gerados são {}'.format(cont2))
print('o percentual de números pares é {}% e o percentual de números impares é {}%'.format(cont3,cont4))
print('o percentual de números ímpares dentre os números gerados que eram menores que 60 é {}'.format(cont5))
print('o maior número par gerado é {}'.format(max(lista, key=int)))
print('o menor número impar gerado {}'.format(min(lista,key=int)))
