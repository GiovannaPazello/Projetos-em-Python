'''Escrever um programa que permita ao usuário digitar três números inteiros. Após
a leitura, o programa deve verificar se os três valores podem formar um triângulo.
Caso possam, o programa deve imprimir uma mensagem especificando se o
triângulo é eqüilátero (três lados iguais), isósceles (dois lados iguais) ou escaleno
(todos os lados diferentes). Obs.: Para que três lados formem um triângulo,
o comprimento de cada um dos lados tem que ser menor que a soma dos outros
dois.'''

l1 = int(input('Escreva o primeiro lado do triângulo:'))
l2 = int(input('Escreva o segundo lado do triângulo:'))
l3 = int(input('Escreva o terceiro lado do triângulo:'))
if ((l1+l2) > l3) and ((l1+l3) > l2) and ((l2+l3) > l1):
    print('Forma um triângulo.')
    if (l1 == l2) and (l1 == l3) and (l2 == l3):
        print('Triângulo equilátero.')
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):
        print('Triângulo isósceles.')
    else:
        print('Triângulo escaleno.')
else:
    print('Não forma um triângulo.')