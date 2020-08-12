def nome_mes(mes):
    numero_mes = int(mes)
    if numero_mes < 1 or numero_mes > 12:
        return 'mes invalido'
    meses = ['janeiro', 'fevereiro', 'março',
    'abril', 'maio', 'junho', 
    'julho', 'agosto', 'setembro',
    'outubro', 'novembro', 'dezembro']
    return meses[numero_mes -1]

def eh_data_valida(data):
    return True

data = input('data de nascimento: ')

#elementos_da_data = []
#
#data.find("-") >= 0:
#    elementos_da_data = data.split("-")
#elif data.find("/") >= 0:
#    elementos_da_data = data.split("/")

elementos_da_data =data.split("/")

print(f'Você nasceu em {elementos_da_data[0]} de {nome_mes(elementos_da_data[1])} de {elementos_da_data[2]}')

