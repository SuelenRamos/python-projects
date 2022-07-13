# algoritmo para determinar a excluvisidade de uma string

def exclusive(w):
    letras = []

    for letra in w:
        if letra not in letras:
            letras.append(letra)
        else:
            return False
    return True

def repeated(sr):
    letras1 = []
    letras_repetidas = []

    # checagem da existência de letras repetidas
    for letra in sr:
        if letra not in letras1:
            letras1.append(letra)

        elif letra not in letras_repetidas:
            letras_repetidas.append(letra)

    return letras_repetidas


word = input('Digite uma string: ')

result = exclusive(word.lower())

if result == True:
    print('A string "%s" possui todos os caracteres exclusivos.' %word)
else:
    print('A string "%s" não possui todos os caracteres exclusivos.' %word)

    print('As letras repetidas foram: ', repeated(word.lower()) )





