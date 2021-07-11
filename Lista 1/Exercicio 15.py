'''Crie um algoritmo que leia a idade de uma pessoa e informe a sua classe eleitoral:
a. não eleitor (abaixo de 16 anos);
b. eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
c. eleitor facultativo (eleitor entre 16 até 18 anos ou eleitor maior de 65
anos, inclusive).'''

i = int(input('Digite sua idade:'))
if i < 16:
    print('Não eleitor.')
elif 18 <= i <= 65:
    print('Eleitor obrigatório.')
else:
    print('Eleitor facultativo.')