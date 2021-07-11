'''Faça um programa para informatizar o cadastro de produtos em uma loja.
Você deve cadastrar produtos até o preço 0 ser cadastrado. Cada produto deve ser armazenado com as
seguintes informações: nome, preço, quantidade e categoria (“L” para luxo e “C” para comum). Depois de
cadastrados os produtos informe:

- a quantidade de produtos de luxo com preço menor que R$ 2000,00

- o preço médios dos produtos de luxo

- o nome do produto mais caro com quantidade menor que 50.

- o percentual de produtos que custam entre R$ 100,0 e R$ 200,00.

- o nome do produto comum mais barato'''

preco = -1
qqntProdLmenor2000 = 0
cont = 0
somaPreco = 0
produtoMaisCaro = 0
nomeProdutoMaisCaro = ''
contPercentual = 0
produtoMaisBarato = 10000000000000000
nomeProdutoMaisBarato = ''

while preco != 0:
    cont +=1
    nome = input('Digite o nome do produto:')
    quantidade = int(input('Digite a quantidade do produto em estoque:'))
    categoria = input('Digite a categoria L (luxo) ou C (comum):')
    preco = float(input('Digite o preço do produto:'))
    somaPreco = somaPreco + preco

    if (categoria == 'l' or 'L') and (preco < 2000):
        qqntProdLmenor2000 +=1
    if (produtoMaisCaro < preco) and quantidade < 50:
        nomeProdutoMaisCaro = nome
    if 200 > preco > 100:
        contPercentual +=1
    if (categoria == 'C' or 'c') and produtoMaisBarato > preco:
        nomeProdutoMaisBarato = nome

media = somaPreco/cont
percentual = (contPercentual*100)/cont

print('A quantidade de produtos de luxo com preço menor que R$ 2000,00 é {}'.format(qqntProdLmenor2000))
print('O preço médios dos produtos de luxo é {}'.format(media))
print('O nome do produto mais caro com quantidade menor que 50 é {}'.format(nomeProdutoMaisCaro))
print('O percentual de produtos que custam entre R$ 100,0 e R$ 200,00 é {}'.format(percentual))
print('O o nome do produto comum mais barato é {}'.format(nomeProdutoMaisBarato))