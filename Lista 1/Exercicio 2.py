'''Escreva um programa em Python que lê 3 números e escreve o valor do maior.'''
n1 = int(input('Escreva um número:'))
n2 = int(input('Escreva outro número:'))
n3 = int(input('Escreva outro número:'))
if n1 > n2 and n1 > n3:
    print('O número {} é maior'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O número maior é {}'.format(n2))
elif n3 > n1 and n3 > n2:
    print('O número {} é maior'.format(n3))