'''Escreva um algoritmo que leia um número e informe se ele é divisível por 10,
por 5 ou por 2 ou se não é divisível por nenhum deles.'''

n = int(input('Digite um número inteiro:'))
if (n%10 == 0) or (n%5 == 0) or (n%2 == 0):
    print('O número é divisível por 10, 5 ou 2.')
else:
    print('O número não é divisível por 10, 5 ou 2.')