'''Faça um programa que resolva a equação do segundo grau em python, verificando:

 - se existem duas raízes reais

 - se existe uma raiz real

 - não existe solução nos números reais'''

a = int(input('Digite valor de a (não pode ser 0):'))
b = int(input('Digite valor de b:'))
c = int(input('Digite valor de c:'))

x1 = (-b+((b*b-4*a*c)*0.5))/2*a
x2 = (-b-((b*b-4*a*c)*0.5))/2*a

if (x1 < 0) and (x2 < 0):
    print('Não existe solução nos números reais.')
elif x1 == x2:
    print('Existe uma raiz real, que é {}'.format(x1))
elif x1 != x2:
    print('Existem duas raízes reais que são x1={} e x2={}'.format(x1,x2))