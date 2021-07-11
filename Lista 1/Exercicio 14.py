''' Escrever um programa que leia a idade de três indivíduos e determine se a soma
das três idades é maior ou igual a 100 anos. Se for, o programa deve imprimir a
mensagem “maior ou igual a 100”, ou a mensagem “menor que 100” deve ser
impressa.'''

i1 = int(input('Escreva a primeira idade:'))
i2 = int(input('Escreva a segunda idade:'))
i3 = int(input('Escreva a terceira idade:'))
s = i1+i2+i3
if s >= 100:
    print('Maior ou igual a 100.')
else:
    print('Menor que 100.')