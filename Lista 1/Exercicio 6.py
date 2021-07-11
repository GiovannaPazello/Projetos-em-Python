'''O índice de Massa Corporal (IMC) é uma fórmula que indica se um adulto está
acima do peso, se está obeso ou abaixo do peso ideal considerado saudável. A
fórmula para calcular o Índice de Massa Corporal é:
IMC = peso / (altura)2
Faça um programa que calcule o IMC de uma pessoa.'''
a = float(input('Digite a altura:'))
p = float(input('Digite o peso:'))
imc = p / (a*a)
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso normal.')
elif 25 <= imc < 30:
    print('Acima do peso.')
elif imc > 30:
    print('Obeso.')