'''Escrever um algoritmo para ler as dimensões de uma cozinha (comprimento,
largura e altura), calcular e escrever a quantidade de caixas de azulejos para
azulejar todas as paredes (considere que não será descontada a área ocupada por
portas e janelas). Cada caixa de azulejos possui 2 metros quadrados.'''

c = float(input('Digite o comprimento:'))
l = float(input('Digite a largura:'))
a = float(input('Digite a altura:'))
mt = (c*l*4)/2
print('A quantidade de caixas para colocar todos os azulejos na cozinha é {}'.format(mt))
