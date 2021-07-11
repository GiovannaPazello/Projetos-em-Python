'''Faça um programa para calcular o fatorial de um número. O usuário deve informar o número para calcular
o fatorial. O programa, deve exibir uma string com a operação e depois o resultado.

Exemplo: Calcular fatorial de : 6

6!= 1*2*3*4*5*6 6!= 720'''

n = int(input('Digite o número:'))
f = 1
i = 2
while i <= n:
    f = f * i
    i = i + 1
print(f)