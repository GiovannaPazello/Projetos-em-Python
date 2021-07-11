Str = input('Digite:')
vogais = 0
espacos = 0
for i in range(len(Str)):
    if Str[i] == ('a' or 'A') and ('e' or 'E') and ('i' or 'I') and ('o' or 'O') and ('U' or 'u'):
        vogais+=1
    elif Str[i] == ' ':
        espacos+=1

print('A quantidade de vogais na frase é {}'.format(str(vogais)))
print('A quantidade de espaços em brancos é {}'.format(str(espacos)))