'''Faça um programa para o usuário adivinhar o número sorteado: O programa deve perguntar o valor
limite para o sorteio (ex: se o usuário informar o número 10, o programa irá sortear um número entre 0 e 10,
inclusive o 10). O programa deve sortear o número e pedir ao usuário que tente adivinhar o número. Caso o usuário
não acerte o palpite o programa deve dizer se o número sorteado é maior ou menor que o informado pelo usuário. O
programa deve continuar pedindo palpites até que o usuário acerte. No final o programa deve informar quantos palpites
foram necessários até que o palpite fosse o correto'''
import random
nLimite = int(input('Digite o número limite para o sorteio:'))
x = random.randint(0,nLimite)
cont = 0

while cont <= nLimite:
    n = int(input('Digite o número que você acha que foi sorteado:'))
    cont+=1
    if n == x:
        print('Parabéns, você acertou o número.')
        break
    elif n > x:
        print('Seu número é maior que o sorteado.')
    else:
        print('Seu número é menor que o sorteado.')

print('A quantidade de tentativas foi {}'.format(cont))
