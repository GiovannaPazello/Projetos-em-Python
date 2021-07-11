'''Escreva um programa em Python que lê 5 valores e conta quantos destes valores
são maiores que 10, escrevendo esta informação na tela.'''
n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))
n4 = int(input('Digite um número:'))
n5 = int(input('Digite um número:'))

cont = 0


if n1 > 10:
    cont += 1
    if n2 > 10:
        cont += 1
        if n3 > 10:
            cont += 1
            if n4 > 10:
                cont += 1
                if n5 > 10:
                    cont += 1
print('A quantidade de números maiores que 10 é {}'.format(cont))