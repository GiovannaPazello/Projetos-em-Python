'''Faça um programa para informatizar o cadastro dos pacientes em um hospital.
Você deve cadastrar os pacientes com as seguintes informações:
nome, idade, sexo (M ou F) e peso. Após terminado o cadastro,
perguntar se o usuário deseja cadastrar mais alunos. Caso ele responda “sim” outro cadastro deve ser efetuado.
Do contrário, deve ser informado:

- o nome do paciente mais velho e com peso maior que 50 quilos.

- peso médio dos pacientes do sexo feminino com mais de 30 anos.

- a quantidade de pacientes do sexo masculino ou com idade menor que 45 anos.

- o percentual de pacientes (masculino ou feminino) que são idosos (mais de 59 anos).'''

qqntPaciente = 0
resposta = 'sim'
contIdade = 0
nomePaciente = ''
somaPesoFemininoMais30 = 0
qqntSexoF = 0
qqntPacientesM45 = 0
contIdosos = 0
while resposta == 'sim':
    print('Paciente #' + str(qqntPaciente+1))
    nome = input('Digite o nome do paciente:')
    idade = int(input('Digite a idade do paciente:'))
    sexo = input('Digite o sexo (M ou F):')
    peso = float(input('Digite o peso:'))

#Nome do paciente mais velho e com peso maior que 50kg
    if idade > contIdade and peso > 50:
        contIdade = idade
        nomePaciente = nome
#peso médio dos pacientes do sexo feminino com mais de 30 anos
    if sexo == 'F' and idade > 30:
        somaPesoFemininoMais30 = somaPesoFemininoMais30 + peso
        qqntSexoF = qqntSexoF +1
#a quantidade de pacientes do sexo masculino ou com idade menor que 45 anos
    if sexo == 'M' and idade < 45:
        qqntPacientesM45 = qqntPacientesM45 +1
#o percentual de pacientes (masculino ou feminino) que são idosos (mais de 59 anos)
    if idade > 59:
        contIdosos = contIdosos+1
    resposta = input('Deseja continuar (sim/não) ?')

media = somaPesoFemininoMais30/qqntSexoF
porcentagem = (contIdosos*100)/qqntPaciente
print('Nome do paciente mais velho e com peso maior que 50 kg {}'.format(nomePaciente))
print('O peso médio dos pacientes do sexo feminino com mais de 30 anos é {}'.format(media))
print('A quantidade de pacientes do sexo masculino ou com idade menor que 45 anos é {}'.format(qqntPacientesM45))
print('O percentual de pacientes (masculino ou feminino) que são idosos (mais de 59 anos) é {}'.format(porcentagem))