'''Um motorista de taxi deseja calcular o rendimento de seu carro na
praça.
Sabendo-se que o preço do combustível é de R$2,50, escreva um programa
para ler:
- a marcação do odômetro no início do dia
- a marcação no final do dia
- o número de litros de combustível gasto
- o valor total (R$) recebido dos passageiros.
Calcule e escreva a média do consumo em Km/l e o lucro líquido do dia. Se o
lucro líquido no dia for inferior a R$ 100,00 exiba a mensagem que o
taxista precisa melhorar seu desempenho.'''
odometroInicio = int(input('Escreva o km do odômetro no início do dia:'))
odometroFinal = int(input('Escreva o km do odômetro no final do dia:'))
litrosCombustivel = int(input('Escreva o litros de combustível gasto do dia:'))
valorTotal = float(input('Escreva o valor total recebido dos passageiros:'))

kmPercorrido = odometroInicio-odometroFinal
media = kmPercorrido/litrosCombustivel
valorCombustivel = litrosCombustivel*2.5
lucroLiquido = valorTotal-valorCombustivel

if lucroLiquido<100:
    print('Taxista precisa melhorar seu desempenho.')
else:
    print('Lucro liquido maior que 100.')