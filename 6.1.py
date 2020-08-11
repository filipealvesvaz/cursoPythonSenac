def tamanho_texto(texto, texto2):
    if len(texto1) == len(texto2):
        print('tamanhos iguais')
    else:
        print('tamanhos diferentes')

def possui_mesmo_conteudo(texto1, texto2):
    if texto1.lower() == texto2.lower():
        print('textos iguais')
    else:
        print('textos diferentes')
    
texto1 = input('informe o texto 1: ')
texto2 = input('informe o texto 2: ')

print(texto1, ":", len(texto1), 'caracteres')
print(texto2, ":", len(texto2), 'caracteres')

tamanho_texto(texto1, texto2)
possui_mesmo_conteudo(texto1, texto2)