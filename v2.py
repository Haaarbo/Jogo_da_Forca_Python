from os import system, name
import random
from json import load


#limpa tela
def limpa_tela() -> None:
    #nt caso seja windows, senao entende-se que se trata de outro so
    _ = system('cls') if name == 'nt' else system('clear')


class Hangman:
    #atributos
    chances = 6
    hangman_draw = ['''

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


    #metodos

    #cosntrutor
    def __init__(self, nome, palavra_sorteada):
        self.nome = nome
        #acesso ao arquivo com a base das palavras e sorteio da palavra
        self.palavra_sorteada = random.choice(load(open('words.json', 'r', encoding='utf-8')))
        self.letras_tentadas = []
        self.letras_erradas = []

    #retornar o nome do usuario
    def get_nome(self):
        return self.nome

    #adivinha palavra
    def tentativa(self, letra):
        self.chances -= 1
        #se esta letra na palavra mas nao foi tentada ainda
        if letra in self.palavra and letra not in self.letras_tentadas:
            self.letras_tentadas.append(letra)
        #se esta letra nao esta na palavra mas nao foi tentada ainda
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        #se nao caber em nenhum dos casos acima:
        else:
            return False
        
        return True
    
    #verifica se o jogo acabou
    def check_game_over(self):
        #faz uma soma binaria, verifica se o jogador venceu(0 ou 1) e se a quantidade de letras erradas atingiu o limite
        return self.check_win or (len(self.letras_erradas) == self.chances)

    
    def check_win(self):
        if
        
        


#start

#cria objeto Hangman
fc1 = Hangman(input('Oi, bem-vindo(a), insira seu nome: '))
print(fc1.get_nome())


print(palavra_sorteada)