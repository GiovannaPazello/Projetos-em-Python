''' Escreva um algoritmo que dada a idade de uma pessoa, determine
sua classificação segundo o seguinte:
a. maior de idade;
b. menor de idade;
c. pessoa idosa (idade superior ou igual a 65 anos).'''
i = int(input('Digite sua idade:'))
if i < 18:
    print('Menor de idade.')
elif 18 <= i > 65:
    print('Maior de idade.')
else:
    print('Pessoa idosa.')