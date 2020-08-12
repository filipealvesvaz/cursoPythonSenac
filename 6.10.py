dezenas = ['', '', 'vinte', 'trinta', 'quarenta',
'cinquenta', 'sessenta', 'setenta', 'oitenta' , 'noventa']
primeira_dezena = ['dez', 'onze', 'doze', 'treze', 'catorze',
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
unidades = ['zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove']

numero = int(input('Informe um número: '))
if (numero < 0) or (numero > 99):
    print('O número informado deve estar entre 0 e 99')
else:
    dezena = numero / 10
    unidade = numero % 10
    
    if (numero >= 20):
        print('%s' % dezenas[dezena])
        if (unidade != 0):
            print('e %s' % unidades[unidade])
        print
    elif (numero >= 10):
        print('%s' % primeira_dezena[unidade])
    else:
        print('%s' % unidades[unidade])