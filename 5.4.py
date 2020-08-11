def avaliar(caractere):
    if caractere > 0:
        return 'P'
    else:
        return 'N'

caractere = float(input('Informe o valor:'))
print(avaliar(caractere))