from os import system, name
import random
from json import dumps

#limpa tela
def limpa_tela() -> None:
    #nt caso seja windows, senao entende-se que se trata de outro so
    _ = system('cls') if name == 'nt' else system('clear') 
    

def checagem_tentativa():
    pass


#inicia game
def game() -> None:
    #intro
    print('Bem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')
    print('-'*20)

    #palavras que podem ser sorteadas
    palavras: str = dumps('words.json')

    #sorteio da palavra
    palavra_sorteada: str = random.choice(palavras)
    #cria lista vazia para armazenar letras adivinhadas
    letras_tentadas = list()
    #definindo qtd de tentativas
    chances: int = 6
    
    #enquanto nao acertar ou acabar as chances, segue
    for tentativas in range(chances, 0, -1):
        print(f'Chances: {tentativas}\nLetras erradas:')
        
