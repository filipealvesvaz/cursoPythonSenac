frase = input('informe uma frase: ') 

fraseSEspaco = frase.replace(" ", "")
vetorFrase = list(fraseSEspaco)
vetorFrase.reverse()

frase2 = ''.join(vetorFrase)

if frase2 == fraseSEspaco:
    print("É um palindromo!")
else:
    print("Não é um palindromo!")