'''Faça um programa para cadastrar os alunos. Para cada aluno deve ser cadastrado seu nome, nota de prova,
nota de trabalho e frequência. Crie um menu no qual o usuário pode:

- inserir um novo aluno
- listar os dados de todos os alunos
- calcular a média final do aluno considerando que a prova tem peso de 70% e o trabalho de 30%.
- dado o nome de um aluno informar sua média final
- criar uma lista com o nome de todos os alunos que tiveram média maior que 8
- informar o status de cada aluno. O status deve ser:
·        Aprovado: média final >= 6 e frequência >= 75%
·        IFA: 4 <= média final < 6 e frequência >=75%
·        Reprovado: média < 4 ou frequência <75%'''

nomeAlunos = []
notaProvas = []
notaTrabalhos = []
listaFrequencia = []
listaMedia = []
nomeListaMedia = []
opcao = -1
dadosAlunos = 0

while opcao != 0:
    #Menu
    print('Digite 1 para inserir o aluno.')
    print('Digite 2 para listar os dados de todos os alunos.')
    print('Digite 3 para mostrar a média do aluno.')
    print('Digite 4 para mostrar os alunos com média maior que 8.')
    print('Digite 5 para mostrar o status do aluno.')
    print('Digite 0 para sair.')
    opcao = int(input('Digite a opção:'))

    #inserir um novo aluno
    if opcao == 1:
        nomeAluno = input('Digite o nome do aluno:')
        nomeAlunos.append(nomeAluno)
        notaProva = float(input('Digite a nota da prova:'))
        notaProvas.append(notaProva)
        notaTrabalho = float(input('Digite a nota do Trabalho:'))
        notaTrabalhos.append(notaTrabalho)
        frequencia = int(input('Digite a frequência:'))
        listaFrequencia.append(frequencia)

    #listar os dados de todos os alunos
    elif opcao == 2:
        dadosAlunos = len(listaFrequencia)
        for i in range(dadosAlunos):
            print('Aluno #' + str(i+1))
            print('Nome:' + nomeAlunos[i])
            print('Nota da prova:' + str(notaProvas[i]))
            print('Nota trabalho:' + str(notaTrabalhos[i]))
            print('Frequência:' + str(listaFrequencia[i]))

    #calcular a média final do aluno considerando que a prova tem peso de 70% e o trabalho de 30%.
    #dado o nome de um aluno informar sua média final
    elif opcao == 3:
        mediaAlunos = len(listaFrequencia)
        for a in range(mediaAlunos):
            print('Aluno #' + str(a+1))
            print('Nome:' + nomeAlunos[a])
            media = (notaTrabalhos[a]*0.3) + (notaProvas[a]*0.7)
            print('Média:' + str(media))
            listaMedia.append(media)

    #criar uma lista com o nome de todos os alunos que tiveram média maior que 8
    elif opcao == 4:
        mediaAluno = len(listaFrequencia)
        for b in range(mediaAluno):
            media = (notaTrabalhos[b] * 0.3) + (notaProvas[b] * 0.7)
            if media > 8:
                nomeListaMedia.append(nomeAlunos[b])
                print(nomeListaMedia)

    #informar o status de cada aluno.
    elif opcao == 5:
        dadosAluno = len(listaFrequencia)
        for c in range(dadosAluno):
            print('Aluno #' + str(c + 1))
            print('Nome:' + nomeAlunos[c])
            print('Media:' + str(listaMedia[c]))
            print('Frequência:' + str(listaFrequencia[c]) + '%')
            if listaFrequencia[c] >= 75 and listaMedia[c] >= 6:
                print('Aprovado!')
            elif listaFrequencia[c] >= 75 and (4 <= listaMedia[c] < 6):
                print('IFA.')
            else:
                print('Reprovado.')



