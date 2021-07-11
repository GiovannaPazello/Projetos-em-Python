'''Escrever um programa que permita ao usuário digitar uma data (dia e mês); em
seguida, o programa deve calcular a quantidade de dias que falta para o final do
ano. Suponha que todos os meses do ano possuem 30 dias.'''

dia = int(input('Digite o dia de hoje:'))
mes = int(input('Digite o mês atual:'))
finalAno = ((12-mes)*30)+(30 - dia)
print('Faltam {} dias para o final do ano'.format(finalAno))