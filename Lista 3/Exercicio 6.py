'''Faça um programa que leia um número digitado pelo usuário. Depois, informe todos os
números primos gerados até o número digitado pelo usuário.'''

n = int(input("Verificar números primos até:"))
cont=0
nPrimos = []

for i in range(2,n):
    if (n % i == 0):
        cont += 1

if(cont==0):
    nPrimos.append(n)

print(nPrimos)