'''Escreva um programa que calcula o valor de lotes imobiliários em duas cidades,
São Paulo e Curitiba. O programa deve perguntar qual o tamanho do lote (lado e
comprimento). A partir desses valores, calcule e exiba quantos metros quadrados
tem o lote. Pergunte em que cidade está localizado o lote (São Paulo ou Curitiba).
Depois, calcule e exiba o valor do lote sabendo que, se estiver em São
Paulo custará R$ 500,00 o metro quadrado e se estiver em Curitiba custará R$
450,00 o metro quadrado.'''

l = float(input('Largura do lote:'))
c = float(input('Comprimento do lote:'))
a = l*c
print('A área do lote é {}'.format(a))
b = input('Localização do lote:')
if b == 'São Paulo':
    print('O valor do lote em São Paulo é R${}'.format(a*500))
elif b == 'Curitiba':
    print('O valor do lote em Curitiba é R${}'.format(a*450))
else:
    print('Essa cidade não têm valor de lote ou você digitou errado.')