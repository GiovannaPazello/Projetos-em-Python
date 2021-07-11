'''Faça uma lista com 50 posições imaginando que cada elemento da lista seja uma pessoa.
Em cada posição você deve gerar randomicamente a idade dessa pessoa. Feito isso informe:

- qual a população de jovens. Considerar jovens as pessoas entre 1 e 20 anos

- qual o percentual de idosos. Considerar idosos as pessoas acima de 60 anos.

- considerando que o corona vírus não causou a morte de nenhuma pessoa abaixo de 10 anos de idade no mundo,
informe qual o percentual de pessoas que não tem risco de morte pelo covid-19.

- considerando que a taxa de mortalidade para pessoas idosas segundo o texto abaixo em itálico, informe a
probabilidade de haver algum óbito na população: “Enquanto entre 0 e 49 anos ela não passa de 1%, entre 50 e 59
fica em 1,3%, entre 60 e 69 vai para 3,6%, entre 70 e 79 anos sobe para 8% e acima dos 80 chega a 14,8%”'''

from random import randint
#Listas
listaPessoas = []
listaJovens = []
listaIdosos = []
listaSemRisco = []
listaComRisco1 = []
listaComRisco2 = []
listaComRisco3 = []
listaComRisco4 = []
for i in range(50):
    idadeGerada = randint(1,100)
    listaPessoas.append(idadeGerada)
    if idadeGerada < 20:
        listaJovens.append(idadeGerada)
    if idadeGerada > 60:
        listaIdosos.append(idadeGerada)
    if idadeGerada < 10:
        listaSemRisco.append(idadeGerada)
    if 50 < idadeGerada < 59:
        listaComRisco1.append(idadeGerada)
    if 60 < idadeGerada < 69:
        listaComRisco2.append(idadeGerada)
    if 70 < idadeGerada < 79:
        listaComRisco3.append(idadeGerada)
    if idadeGerada > 80:
        listaComRisco4.append(idadeGerada)

print('A quantidade de jovens é {}'.format(len(listaJovens)))
#Porcentagem Idosos
a = len(listaPessoas)
b = len(listaIdosos)
porcentagemIdosos = (b*100)/a
print('A porcentagem de idosos é {}%'.format(porcentagemIdosos))
#Porcentagem crianças -10 anos sem risco de morte
c = len(listaSemRisco)
porcentagemSemRisco = (c*100)/a
print('A porcentagem de pessoas sem risco de morte é {}%'.format(porcentagemSemRisco))
#Probabilidade da quantidade de pessoas morrerem por covid
d = len(listaComRisco1)
e = len(listaComRisco2)
f = len(listaComRisco3)
g = len(listaComRisco4)
probabilidade = ((d*1.3) + (e*3.6) + (f*8) + (g*14.8))/a
print('A probabilidade de mortes por covid é {}%'.format(probabilidade))
