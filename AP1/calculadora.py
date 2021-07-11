print('Calculadora')
nro1 = int(input("Digite o primeiro número: "))
nro2 = int(input("Digite o segundo número: "))

print("Menu")
print("1 - somar")
print("2 - subtrair")
print("3 - multiplicar")
print("4 - divisao")
operacao = int(input("Digite a opcao que deseja: "))

if operacao == 1:
    soma = nro1 + nro2
    print("resultado: " + str(soma))
if operacao == 2:
    subtracao = nro1 - nro2
    print("resultado: " + str(subtracao))