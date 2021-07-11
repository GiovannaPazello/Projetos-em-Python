class suicidios():
    def __init__(self):
        self.estado = ""
        self.ano = 0
        self.circobito = ""
        self.dtobito = 0
        self.dtnascimento = 0
        self.sexo = ""
        self.racacor= ""
        self.estciv = ""
        self.esc = 0
        self.ocup = ""
        self.cidade = ''
        self.idade = 0

matriz = []

def criarMenu():
    print('Menu')
    print('1 - Carregar dados do arquivo') 
    print('2 - Listar todos os dados')
    print('3 - Informar a média de idade dos casos de suicídio no estado de Goiás.')
    print('4 - Informar as três profissões que mais tiveram morte por suicídio.')
    print('5 - Informar a quantidade de suicídio por estado')
    print('6 - Informar para cada estado da região sul como variou a taxa de suicídio entre os anos de 2014 e 2018')
    print('7 - Informe qual o estado civil que mais teve casos de suicídio.')
    print('8 - Dentre os homens, qual a profissão que mais teve casos de suicídio no estado de Minas Gerais?')
    print('9 - Pergunte ao usuário um estado. Depois, verifique nesse estado qual a distribuição dos casos de suicídio em relação a escolaridade das vítimas.')
    print('10 - Qual a cidade de cada região do país que mais teve casos de suicídio em 2018?')
    print('11 - Qual a raça que mais foi vítima de homicídio no Rio de Janeiro?')
    print('12 - Qual o percentual de vítimas de acordo com as raças?')
    print('13 - Considere as seguintes categorias:')
    print('a. Mulher – Branca') 
    print('b. Mulher – Parda')
    print('c. Mulher – Preta')
    print('d. Mulher – Amarela')
    print('e. Homem – Branca')
    print('f. Homem – Parda')
    print('g. Homem – Preta')
    print('h. Homem – Amarela')
    print('14 - Informe o percentual de vítimas de homicídio de cada categoria. Informe também o percentual de vítimas de suicídio das mesmas categorias')
    print('15 - Crie outra pesquisa que julgar fazer sentido para o escopo do projeto. - Pergunte ao usuário um estado. Depois, verifique nesse estado qual a distribuição dos casos de suicídio em relação a idade das vítimas.')

def carregarDoArquivo(): #1 (rodando)
    arquivo = open('arquivo_suicidio.csv', 'r')
    arquivo.readline()
    for linha in arquivo:
        s = suicidios()
        linha = linha.replace('\n','')
        dados = linha.split(',')
        s.estado = dados[0]
        s.ano = int(dados[1])
        s.circobito = dados[2]
        s.dtobito = dados[3]
        s.dtnascimento = dados[4]
        s.sexo = dados[5]
        s.racacor = dados[6]
        s.estciv = dados[7]
        s.esc = dados[8]
        s.ocup = dados[9]
        s.cidade = dados[10]
        try:                
            s.idade = int(dados[len(dados)-2])
        except ValueError:
            s.idade = 0
        matriz.append(s)
    arquivo.close()
    return matriz

def listarDados(matriz): #2 (rodando)
    for i in matriz:
        print('Estado:', i.estado, 'Ano:', i.ano,'Como morreu:', i.circobito, 'Data da morte:', i.dtobito, 'Data nascimento:', i.dtnascimento, 'Sexo:', i.sexo, 'Raca/Cor:', i.racacor, 'Estado civil:', i.estciv, 'Escolaridade:', i.esc, 'Ocupação:', i.ocup, 'Idade:', i.idade)

def encontrarMediaIdadeGoias(matriz): #3 (rodando)
    somaIdade = 0
    qttdGoias = 0
    for elemento1 in matriz:
        if elemento1.estado == 'GO':
            somaIdade += elemento1.idade
            if elemento1.idade != 0:
                qttdGoias +=1
    media = 0
    if qttdGoias > 0:
        media = somaIdade/qttdGoias
    print(f"A populacao do estado Goias tem a media de: {media:.2f} idade")

def encontrarProfissoesMaisMorte(matriz): #4(rodando)
    dic = {}
    lista = [0, 0 , 0]
    listaProfissao = ['', '', '']
    for i in matriz:
        if i.ocup in dic:
            dic[i.ocup] += 1
        else:
            dic[i.ocup] = 1
    del dic['0']
    for key in dic.keys():
        if dic[key] > lista[0]:
            lista[0] = dic[key]
            listaProfissao[0] = key
        elif dic[key] > lista[1]:
            lista[1] = dic[key]
            listaProfissao[1] = key
        elif dic[key] > lista[2]:
            lista[2] = dic[key]
            listaProfissao[2] = key
    print(listaProfissao)

def verificarEstado(matriz): #5 (rodando)
    listaEstado = []
    for elemento in matriz:
        if elemento.estado not in listaEstado:
            listaEstado.append(elemento.estado)
    return listaEstado

def qttdSuicidioEstado(matriz): #5 (rodando)
    qttSuicidioEstado = verificarEstado(matriz)
    listaEstado = []
    listaMortes = []
    for elemento1 in qttSuicidioEstado:
        listaEstado.append(elemento1)
        cont = 0
        for elemento2 in matriz:
            if elemento1 == elemento2.estado:
                cont+=1
                listaMortes.append(cont)
                
        print(f"Estado: {elemento1} tem {cont} suicidios")
    

def regiaoSulTaxaSuicidio(matriz): #6 (rodando)
    cont = 0
    lista = []
    for elemento in matriz:
        if elemento.estado not in lista:
            lista.append(elemento.estado)
        if elemento.estado == 'PR' or elemento.estado == 'SC' or elemento.estado == 'RS':
            if elemento.ano >= 2014 and elemento.ano <= 2018:
                cont += 1
    taxa = (cont*100)/(len(matriz))
    print(f'A taxa de suicidio da região sul é {taxa:.2f}')

def verificarEstadoCivil(matriz): #7 (rodando)
    listaEstadoCivil = []
    for elemento in matriz:
        if elemento.estciv not in listaEstadoCivil:
            listaEstadoCivil.append(elemento.estciv)
    return listaEstadoCivil

def estadoCivilComMaisSuicidio(matriz): #7 (rodando)
    qttSuicidioEstadoCivil = verificarEstadoCivil(matriz)
    listaEstadoCivil = []
    listaMortes = []
    for elemento1 in qttSuicidioEstadoCivil:
        listaEstadoCivil.append(elemento1)
        cont = 0
        for elemento2 in matriz:
            if elemento1 == elemento2.estciv:
                cont+=1
                listaMortes.append(cont)
    print(f"Estado civil: {elemento1} tem {cont} suicidios")

def procuraProfissao(matriz): #8 (rodando)
    listaProfissao = {}
    for elemento in matriz:
        if elemento.ocup not in listaProfissao:
            listaProfissao[elemento.ocup] = 0
    return listaProfissao

def homensProfissaoSuicidioMinasGerais(matriz): #8 (rodando)
    profissao = procuraProfissao(matriz)
    maior = 0
    ocupacao = ''
    for elemento in matriz:
        if elemento.sexo == 'Masculino' and elemento.estado == 'MG':
            profissao[elemento.ocup] +=1
    del profissao['0'] #Existe a profissao 0 no arquivo
    for key in profissao.keys():
        if profissao[key] > maior:
            ocupacao = key
            maior = profissao[key]

    print(f'Em Minas Gerais tem {maior} suicidios por homens na profissao {ocupacao}')


def estadoSuicidioEEscolaridade(lugar, matriz): #9 (rodando)
    dic = {}
    for elemento in matriz:
        if elemento.estado == lugar:
            if elemento.esc in dic:
                dic[elemento.esc]+=1
            else:
                dic[elemento.esc] = 0
    print(dic)



def cidadeRegiaoSuicidio2018(matriz): #10
    regioes = {
        'Sul':{},
        'Norte':{},
        'Nordeste':{},
        'CentroOeste':{},
        'Sudeste':{}
    }
    for elemento in matriz:
        if elemento.estado == 'AC' or elemento.estado == 'RO' or elemento.estado == 'AM' or elemento.estado == 'RR' or elemento.estado == 'PA' or elemento.estado == 'AP' or elemento.estado == 'TO':            
            if elemento.cidade in regioes['Norte']:
                regioes['Norte'][elemento.cidade] +=1
            else:
                regioes['Norte'][elemento.cidade] = 1
        elif elemento.estado == 'MA' or elemento.estado == 'PI' or elemento.estado == 'CE' or elemento.estado == 'BA' or elemento.estado == 'RN' or elemento.estado == 'PB' or elemento.estado == 'PE' or elemento.estado == 'AL' or elemento.estado =='SE':
            if elemento.cidade in regioes['Nordeste']:
                regioes['Nordeste'][elemento.cidade] +=1
            else:
                regioes['Nordeste'][elemento.cidade] = 1
        elif elemento.estado == 'MT' or elemento.estado == 'GO' or elemento.estado == 'MS':
            if elemento.cidade in regioes['CentroOeste']:
                regioes['CentroOeste'][elemento.cidade] +=1
            else:
                regioes['CentroOeste'][elemento.cidade] = 1
        elif elemento.estado == 'SP' or elemento.estado == 'RJ' or elemento.estado == 'MG' or elemento.estado == 'ES':
            if elemento.cidade in regioes['Sudeste']:
                regioes['Sudeste'][elemento.cidade] +=1
            else:
                regioes['Sudeste'][elemento.cidade] = 1
        elif elemento.estado == 'PR' or elemento.estado == 'SC' or elemento.estado == 'RS':
            if elemento.cidade in regioes['Sul']:
                regioes['Sul'][elemento.cidade] +=1
            else:
                regioes['Sul'][elemento.cidade] = 1
    for key in regioes.keys():
        maior = 0
        lugar = ''
        for chave in regioes[key].keys():
            if regioes[key][chave] > maior:
                lugar = chave
                maior = regioes[key][chave]

        print(f'A cidade {lugar} da região {key} teve um total de suicidios {maior} maior que as outras cidades')

def procuraRacaESexo(matriz, sexo, circobito): #11
    for elemento in matriz:
        if elemento.circobito == circobito:
            if elemento.racacor not in sexo[elemento.sexo]:
                sexo[elemento.sexo][elemento.racacor] = 1
            else:
                sexo[elemento.sexo][elemento.racacor] += 1

    return sexo

def procuraRaca(matriz): #11
    listaRaca= {}
    for elemento in matriz:
        if elemento.racacor not in listaRaca:
            listaRaca[elemento.racacor] = 0
    return listaRaca

def racaVitimaHomicidioRio(matriz): #11
    raca = procuraRaca(matriz)
    maior = 0
    cor = ''
    for elemento in matriz:
        if elemento.estado == 'RJ' and elemento.circobito == 'Homicídio':
            raca[elemento.racacor] +=1
    for key in raca.keys():
        if raca[key] > maior:
            cor = key
            maior = raca[key]

    print(f'No Rio de Janeiro a raca {cor} é a que mais tem morte por homicidio, com {maior} homicidios.')
    
def percentualVitimasRacas(matriz): #12
    raca = procuraRaca(matriz)
    for elemento in matriz:
        raca[elemento.racacor] +=1
    for key in raca.keys():
        raca[key] +=1

        print(f"A raca {key} tem o percentual de: {(raca[key] / len(matriz))*100:.2f}%")

def procuraSexo(matriz): #13
    listaSexo= {}
    for elemento in matriz:
        if elemento.sexo not in listaSexo:
            listaSexo[elemento.sexo] = {}
    return listaSexo

def percentualVitimasHomicidio(matriz): #13
    sexo = procuraSexo(matriz)
    sexo = procuraRacaESexo(matriz, sexo, 'Suicídio')
    print(sexo)
    for chave in sexo.keys():
        for key in sexo[chave].keys():
            print(f"Raca:{key}, Sexo:{chave}, Porcentagem:{(sexo[chave][key] / len(matriz))*100:.2f}%")


def percentualVitimasSuicidio(matriz): #14
    sexo = procuraSexo(matriz)
    sexo = procuraRacaESexo(matriz, sexo, 'Homicídio')
    print(sexo)
    for chave in sexo.keys():
        for key in sexo[chave].keys():
            print(f"Raca:{key}, Sexo:{chave}, Porcentagem:{(sexo[chave][key] / len(matriz))*100:.2f}%")


def estadoSuicidioEstadoCivil(lugar,matriz): #15
    dic = {}
    for elemento in matriz:
        if elemento.estado == lugar:
            if elemento.estciv in dic:
                dic[elemento.estciv]+=1
            else:
                dic[elemento.estciv] = 0
    print(dic)

opcao = -1
while opcao !=0:
    criarMenu()
    opcao = int(input('Digite a opcao: '))
    if opcao == 1:
        carregarDoArquivo()
    elif opcao == 2:
        listarDados(matriz)
    elif opcao == 3:
        encontrarMediaIdadeGoias(matriz)
    elif opcao == 4:
        encontrarProfissoesMaisMorte(matriz)
    elif opcao == 5:
        qttdSuicidioEstado(matriz)
    elif opcao == 6:
        regiaoSulTaxaSuicidio(matriz)
    elif opcao == 7:
        estadoCivilComMaisSuicidio(matriz)
    elif opcao == 8:
        homensProfissaoSuicidioMinasGerais(matriz)
    elif opcao == 9:
        estado = input('Digite um estado: ')
        linha = estadoSuicidioEEscolaridade(estado, matriz)
    elif opcao == 10:
        cidadeRegiaoSuicidio2018(matriz)
    elif opcao == 11:
        racaVitimaHomicidioRio(matriz)
    elif opcao == 12:
        percentualVitimasRacas(matriz)
    elif opcao == 13:
        percentualVitimasHomicidio(matriz)
    elif opcao == 14:
        percentualVitimasSuicidio(matriz)
    elif opcao == 15:
        estado = input('Digite um estado: ')
        linha = estadoSuicidioEstadoCivil(estado, matriz)


        

