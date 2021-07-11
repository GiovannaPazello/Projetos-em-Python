'''Duas fabricantes de calçado disputam o mercado no Brasil. A empresa A tem produção de 10.000 pares/mês
e um crescimento mensal de 15%. A empresa B, de 8.000 pares/mês e tem um crescimento mensal de 20%. Determinar
o número de meses necessários para que a empresa B supere o número de pares produzidos pela empresa A.'''

a = 10000
b = 8000
qqntMeses = 0
while a > b:
    a = (a*0.15) + a
    b = (b*0.2) + b
    qqntMeses = qqntMeses +1

print(qqntMeses)