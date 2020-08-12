import random

#aleatorio = random.randrange(1, 10)

#Função para jogar os dados
def jogar_dados():
    jogada = random.randint(2, 12)
    return jogada

# Jogo
quantidade_de_jogadas = 1
termina = False
pontos = 0

while not termina:
    
    jogada = jogar_dados()
    
    if quantidade_de_jogadas == 1:
        if jogada == 7 or jogada == 11:
            print(f'Parabéns! Você é um natural e ganhou!!! \o/  {jogada}')
            termina = True
        elif jogada == 2 or jogada == 3 or jogada == 12:
            print(f'Craps! Você perdeu! :( {jogada}')
            termina = True
        elif jogada >= 4 and jogada <= 10:
            pontos = jogada
            print(f'Você tirou {pontos}')
        else:
            if jogada == pontos:
                print(f'Parabéns! Você ganhou em {quantidade_de_jogadas} jogadas')
                termina = True
            elif jogada == 7:
                print(f'Perdeu')
                termina = True
        print(jogada)
        print(quantidade_de_jogadas)
        print('--------------------------')
        
        quantidade_de_jogadas += 1