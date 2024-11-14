from os import system, name
import random
from json import load


#limpa tela
def limpa_tela() -> None:
    #nt caso seja windows, senao entende-se que se trata de outro so
    _ = system('cls') if name == 'nt' else system('clear')


class Hangman:
    #cosntrutor
    def __init__(self, nome) -> None:
        self.nome = nome
        #acesso ao arquivo com a base das palavras e sorteio da palavra
        self.palavra_sorteada = random.choice(load(open('words.json', 'r', encoding='utf-8')))
        self.letras_tentadas = []
        self.letras_erradas = []
        #atributos
        self.chances = 6
        self.hangman_draw = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

    #retornar o nome do usuario
    def get_nome(self) -> str:
        return self.nome

    #adivinha palavra
    def tentativa(self, letra) -> bool:
        self.chances -= 1
        #se esta letra está na palavra mas nao foi tentada ainda
        if letra in self.palavra_sorteada and letra not in self.letras_tentadas:
            self.letras_tentadas.append(letra)
        #se esta letra nao está na palavra mas nao foi tentada ainda
        elif letra not in self.palavra_sorteada and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        #se nao caber em nenhum dos casos acima:
        else:
            return False
        return True
    
    #verifica se o jogo acabou
    def check_game_over(self) -> bool:
        #faz uma soma binaria, verifica se o jogador venceu(0 ou 1) e se a quantidade de letras erradas atingiu o limite
        return self.check_win() or (len(self.letras_erradas) == self.chances+1)

    #verifica se o jogador venceu
    def check_win(self) -> bool:
        if '_' not in self.esconde_palavra():
            return True
        return False
    
    #realiza a ocultacao da palavra sorteada
    def esconde_palavra(self) -> str:
        palavra_escondida = '' #cria uma palavra que sera mostrada que escondera os caracteres
        for letra in self.palavra_sorteada:
            #se uma das letras tentadas estiver na palavra, add, senao, add um '_'
            if letra not in self.letras_tentadas:
                palavra_escondida+='_'
            else:
                palavra_escondida+=letra
        return palavra_escondida
    
    #mostra como ta o jogo: palavras erradas, o hangman, quantas tentativas ja foram
    def game_status(self):
        #imprime o desenho
        print(self.hangman_draw[len(self.letras_erradas)])
        #imprime a palavra ocultada com os caracteres acertados
        print(f'\nPalavra: {self.esconde_palavra()}')
        #imprime as letras erradas, o * serve para desempacotar a lista
        #NAO DA PRA USAR O * NUMA F-STRING
        print('\nLetras erradas: ', *self.letras_erradas, '\n')
        

#start

#cria objeto Hangman
fc1 = Hangman(input('Oi, bem-vindo(a), insira seu nome: '))
print(fc1.get_nome())
while not fc1.check_game_over():
    limpa_tela()

    #print game stts
    fc1.game_status()
    #captura caractere do user e verifica se ta certo
    fc1.tentativa(input('\nDigite uma letra ->'))

print(f'\nA palavra era {fc1.palavra_sorteada}!')
if fc1.check_win():
    print(f'\nParabéns {fc1.get_nome()}, você venceu! :D')
else:
    print(f'\nInfelizmente você perdeu {fc1.get_nome()}. :(')
