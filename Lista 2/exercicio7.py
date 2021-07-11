'''Elabore um programa que mostre os n termos da Série a seguir:
a. S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série. Leia o valor de (n)'''

n = int(input('Digite o valor de n: '))

denominador = 1
linha = 'S = '
S = 0
for i in range (1,n):
    termo = str(i) + '/' + str(denominador)
    S = S + i/denominador
    linha = linha + termo + ' + '
    denominador = denominador + 2

ultimoTermo = str(n) + '/' + str(denominador)
S = S + n/denominador
linha = linha + ultimoTermo
print(linha)
print('Valor da serie: ' + str(S))
