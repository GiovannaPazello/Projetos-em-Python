'''Faça um programa que gere números aleatórios entre 0 e 50 até o número 32 ser
gerado. Quando isso ocorrer, informar:
a. A soma de todos os números gerados
b. A quantidade de números gerados que é impar
c. O menor número gerado'''

import random

x = random.randint(0,50)
cont = 32
somaNumeros = 0
qqntImpares = 0
menorNumero = 51
while cont != x:
    x = random.randint(0, 50)
    somaNumeros = somaNumeros + x
    if x%2 != 0:
        qqntImpares = qqntImpares + 1
    if menorNumero > x:
        menorNumero = x
print('A soma de todos os números é {}'.format(somaNumeros))
print('A quantidade de números ímpares é {}'.format(qqntImpares))
print('O menor número é {}'.format(menorNumero))






