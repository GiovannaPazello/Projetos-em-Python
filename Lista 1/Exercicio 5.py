'''Escreva um programa que permita ao usuário digitar a nota do aluno na prova, a
nota do aluno nos trabalhos e a freqüência do mesmo. O calculo da nota do aluno
é calculada sabendo que a prova tem peso de 70% e o trabalho de 30%. A partir
dos dados abaixo indique se o aluno está aprovado, reprovado ou em recuperação.
- Aprovado: média >= 6.0 e freqüência >=75%
- Recuperação: média >=4.0 e média <6.0 e freqüência>=75%
- Reprovado: média<4.0 ou freqüência <75%'''
np = float(input('Digite a nota da prova:'))
nt = float(input('Digite a nota do trabalho:'))
f = int(input('Digite a frequência:'))

m = (np*0.7) + (nt*0.3)

if m >= 6 and f >= 75:
    print('Aprovado')
elif 4 <= m < 6 and f >= 75:
    print('Recuperação')
else:
    print('Recuperação')