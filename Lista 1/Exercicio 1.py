'''Escreva um programa em Python que lê 2 números e escreve o valor do maior.'''

n1 = int(input('Escreva um número:'))
n2 = int(input('Escreva outro número:'))
if n1 > n2:
    print('O número {} é maior'.format(n1))
elif n2 > n1:
    print('O número maior é {}'.format(n2))