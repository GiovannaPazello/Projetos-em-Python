n = int(input('Digite o valor de n: '))

denominador = 1
linha = 'S = '
S = 0
i = 1
while i < n:
    termo = str(i) + '/' + str(denominador)
    S = S + i/denominador
    linha = linha + termo + ' + '
    denominador = denominador + 2
    i = i + 1

ultimoTermo = str(n) + '/' + str(denominador)
S = S + n/denominador
linha = linha + ultimoTermo
print(linha)
print('Valor da serie: ' + str(S))
