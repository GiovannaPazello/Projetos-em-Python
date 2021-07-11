def criarMenu():
    print('Menu')
    print('0 - sair')
    print('1 - cadastrar cliente')
    print('2 - listar cliente')
    print('3 - cadastrar produto')
    print('4 - listar produtos')
    print('5 - cadastrar venda')
    print('6 - listar vendas')
    print('7 - informar qto cada cliente gastou')

def salvarCliente(nomeCli, telefoneCli, enderecoCli, matriz):
    novoCliente = [nomeCli, telefoneCli, enderecoCli]
    matriz.append(novoCliente)

def listar(matriz):
    tamanho = len(matriz)
    for i in range(tamanho):
        print(matriz[i])

def salvarProduto(nomeP, precoP, matriz):
    novoProduto = [nomeP, precoP]
    matriz.append(novoProduto)

def listarProdutosCompra(matriz):
    tamanho = len(matriz)
    for i in range(tamanho):
        print(str(i+1)+ ' - ' + matriz[i][0] + ' -> ' + str(matriz[i][1]))


def buscarPreco(nomeProd,matriz):
    tam = len(matriz)
    for i in range(tam):
        if matriz[i][0] == nomeProd:
            return matriz[i][1]
    return 0

def salvarVenda(cli, prod, qt, valor, matriz):
    venda = [cli, prod, qt, valor]
    matriz.append(venda)

def exibirGastoPorCliente(matriz):
    dic = {}
    tamanho = len(matriz)
    for i in range(tamanho):
        if matriz[i][0] in dic: #se já existir a chave no dicionario
            dic[matriz[i][0]] = dic[matriz[i][0]] + matriz[i][3]
        else: #se a chave ainda nao existir
            dic[matriz[i][0]] = matriz[i][3]
    return dic



clientes = []
produtos = []
vendas = []
dicQtddMinima = {}
opcao = -1
while opcao !=0:
    criarMenu()
    opcao  = int(input('Digite a opcao: '))
    if opcao  == 1:
        nome = input('Digite o nome do cliente: ')
        telefone = input('Telefone: ')
        endereco = input('Endereço: ')
        salvarCliente(nome,telefone,endereco,clientes)
    elif opcao == 2:
        listar(clientes)
    elif opcao == 3:
        nome = input('Digite o nome do produto: ')
        preco = float(input('Digite o preco do produto: '))
        salvarProduto(nome, preco, produtos)
        qtddMinima = int(input('Digite a qtdd Minima: '))
        dicQtddMinima[nome] = qtddMinima
    elif opcao ==4:
        listar(produtos)
    elif opcao ==5:
        print('Clientes: ')
        listar(clientes)
        nomeCliente = input('Digite o nome do Cliente: ')
        print('Cadastro da lista de compras do Cliente')
        continuar = True
        dicCompras = {}
        while continuar:
            listarProdutosCompra(produtos)
            nomeProd = input('Digite o produto que deseja comprar: ')
            qtddProd = int(input('Digite a qtdd de produtos: '))
            if dicQtddMinima[nomeProd] <= qtddProd:
                dicCompras[nomeProd] = qtddProd
            else:
                print('Vc nao comprou a qtdd minima que era '+str(dicQtddMinima[nomeProd]))
            resposta = input('Deseja continuar (s/n)')
            if resposta != 's':
                continuar = False
        for chave in dicCompras.keys():
            precoProd = buscarPreco(chave, produtos)
            totalPorProduto = precoProd*dicCompras[chave]
            salvarVenda(nomeCliente,chave, dicCompras[chave],totalPorProduto ,vendas)

    elif opcao ==6:
        listar(vendas)
    elif opcao ==7:
        dicGastos = exibirGastoPorCliente(vendas)
        for chave in dicGastos.keys():
            print(chave + ' -> ' + str(dicGastos[chave]))