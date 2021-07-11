string = input('Digite a palavra:')
stringSemEspacos = string.replace(' ', '')
stringTodaMinuscula = stringSemEspacos.lower()
stringInvertida = stringTodaMinuscula[::-1]
if stringInvertida == stringTodaMinuscula:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
