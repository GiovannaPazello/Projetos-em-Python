'''Faça um programa com um menu de opções onde o usuário pode gerenciar listas. Ele irá cadastrar
duas listas e irá manipulá-las de acordo com as opções:

opção 1 - inserir elementos na Lista 1. Os elementos na Lista 1 devem ser inseridos de um em um.
A quantidade máxima de elementos que essa lista deve suportar é de 5 elementos.

opção 2 - inserir elementos na Lista 2. Diferentemente da Lista 1, nesta segunda lista o usuário
deve digitar um número e serão inseridos na lista, além do número digitado, mais 4 elementos sendo que
o segundo é o dobro do primeiro, o terceiro é o dobro do segundo e assim sucessivamente, até completar
5 elementos nesta lista.

opção 3 - exibir o conteúdo das duas listas anteriores.

opção 4 - criar e exibir uma nova lista que é composta pela união dos elementos da duas listas anteriores.
Essa será chamada de ListaUniao

opção 5 - criar e exibir uma lista composta pela intersecção dos elementos das duas listas

opção 6 - encontrar o maior valor das duas listas e somar esse valor aos elementos da primeira lista

opção 7 - multiplicar os elementos de cada posição da primeira lista pelo valor do elemento na
segunda lista, criando e exibindo uma nova lista. Ex: se a primeira lista for  [1,2,3,4,5]
e a segunda for [1,2,4,8,16] o resultado da terceira lista será [1,4,12,32,80].

opção 8 - zerar o conteúdo das duas listas.

opção 9 - ordenar a ListaUniao em ordem decrescente.
Essa opção só poderá ser chamada se a opção 4 já tiver sido chamada.'''
lista1 = []
lista2 = []
listaUniao = []
listaInter = []
multiplicandolistas = []
opcao = -1

while opcao != 0:
    #Menu
    print('Digite 1 para inserir 1 item na lista.')
    print('Digite 2 para inserir mais que um elemento na lista.')
    print('Digite 3 para exibir o conteúdo das duas listas anteriores.')
    print('Digite 4 para criar uma nova lista juntando as duas primeiras listas.')
    print('Digite 5 para criar e exibir uma intersecção dos elementos das duas primeiras listas.')
    print('Digite 6 para encontrar o maior valor das duas listas e somar aos elementos da primeira lista.')
    print('Digite 7 para multiplicar os elementos de cada posição da primeira lista com a segunda lista.')
    print('Digite 8 para zerar o conteúdo das duas listas.')
    print('Digite 9 para ordenar a ListaUniao em ordem decrescente.')
    opcao = int(input('Digite a opção:'))

    #inserir elementos na Lista 1.
    if opcao == 1:
        while len(lista1) < 5:
            primeiraLista = int(input('Digite o número para a lista 1:'))
            lista1.append(primeiraLista)
    #inserir elementos lista 2.
    if opcao == 2:
        numerosdaLista2 = int(input('Digite o número para a lista 2:'))
        lista2.append(numerosdaLista2)
        elementosLista2 = len(lista1)
        for i in range(elementosLista2):
            numerosdaLista2 = lista2[i]*2
    #exibir conteudo das duas listas
    if opcao == 3:
        print(lista1)
        print(lista2)
    #listaUnião
    if opcao == 4:
        listaUniao.append(lista1+lista2)
    #lista Intersecção
    if opcao == 5:
        listaInter = [val for val in lista1 if val in lista2]
    #encontrar o maior valor das duas listas e somar o valor aos elementos da lista 1.
    if opcao == 6:
        maior = max(listaUniao)
        lista1.append(maior)
    #multiplicar os elementos de cada posição da primeira lista pelo valor do elemento na segunda lista
    if opcao == 7:
        numeroslista1 = len(lista1)
        numeroslista2 = len(lista2)
        for a in range(numeroslista1):
            for b in range(numeroslista2):
                resultado = lista1[a]*lista2[b]
                multiplicandolistas.append(resultado)
    #zerar o conteúdo das duas listas
    if opcao == 8:
        lista1.clear()
        lista2.clear()
    #ordenar a ListaUniao em ordem decrescente.
    if opcao == 9:
        if len(listaUniao) > 1:
            listaUniao.sort(reverse=True)

