'''Escrever um programa que permita ao usuário digitar o dia e mês de seu
aniversário e a data de hoje (dia e mês); em seguida, o programa deve calcular
quantos dias faltam entre a data de hoje e a data do próximo aniversário. Suponha
todos os meses com 30 dias.'''

dia = int(input('Digite a data de hoje:'))
mes = int(input('Digite o mes atual (em número):'))
diaNiver = int(input('Digite o dia do seu aniversário:'))
mesNiver = int(input('Digite o mês do seu aniversário:'))

if mesNiver>=mes and diaNiver > dia:
    dataDia = (30-dia)+diaNiver
    dataMes = (mesNiver-(mes+1))*30
    print('Seu aniversário é daqui {} dias'.format(dataDia + dataMes))
elif mesNiver<=mes and diaNiver < dia:
    dataDia = (30 - dia) + diaNiver
    dataMes = (mesNiver + (12 - mes)) * 30
    print('Seu aniversário é daqui {} dias'.format(dataDia + dataMes))
elif mesNiver == mes and diaNiver == dia:
    print('Parabéns pelo seu aniversário.')