palavra1=input("Digite uma palavra: ")
palavra2 = input("Digite um anagrama: ")
stringSemEspacos1 = palavra1.replace(' ', '')
stringTodaMinuscula1 = stringSemEspacos1.lower()
stringSemEspacos2 = palavra2.replace(' ', '')
stringTodaMinuscula2 = stringSemEspacos2.lower()
str_anagrama = ""
for cada_letra in stringTodaMinuscula2:
    if cada_letra in stringTodaMinuscula1:
        str_anagrama = str_anagrama + cada_letra
if str_anagrama == stringTodaMinuscula2:
    print('É um anagrama.')
else:
    print('Não é um anagrama.')
