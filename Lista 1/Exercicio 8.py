'''A prefeitura de Quixeramubim abriu uma linha de crédito para os funcionários
estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
bruto. Fazer um algoritmo que permita entrar com o salário bruto e o valor da
prestação, e informar se o empréstimo pode ou não ser concedido.'''

s = float(input('Digite o valor do salário:'))
c = float(input('Digite o valor do empréstimo:'))
t = int(input('Digite em quantos meses será paga a prestação:'))

p = c/t
b = s*0.3

if p>b:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')
