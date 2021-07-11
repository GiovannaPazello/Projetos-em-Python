#S = 2/4 - 3/9 + 4/16 – 5/25 + 6/36 - .... + n/m

n = int(input('Digite o nro de termos da serie: '))
numerador  = 1
soma = 0
serie = ''
sinal = ' + '
for i in range (n-1):
    numerador = numerador + 1
    denominador  = numerador*numerador

    termo = str(numerador) + '/' + str(denominador)
    if sinal == ' + ':
        sinal = ' - '
        soma = soma + numerador/denominador
    else:
        sinal = ' + '
        soma = soma - numerador/denominador
    serie = serie + termo + sinal

numerador = numerador + 1
denominador  = numerador*numerador
termo = str(numerador) + '/' + str(denominador)
serie = serie + termo

if sinal == ' + ':
    soma = soma + numerador/denominador
else:
    soma = soma - numerador/denominador
print(serie)
print('valor da serie: ' + str(soma))


