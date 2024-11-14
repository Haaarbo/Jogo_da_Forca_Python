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
    def check_game_over(self) -> bool:
        #faz uma soma binaria, verifica se o jogador venceu(0 ou 1) e se a quantidade de letras erradas atingiu o limite
        return self.check_win or (len(self.letras_erradas) == self.chances)

    
    def check_win(self) -> bool:
        if '_' not in self.esconde_palavra():
            return True
        return False
    
    def esconde_palavra(self) -> str:
        palavra_escondida = '' #cria uma palavra que sera mostrada que escondera os caracteres
        for letra in self.palavra_sorteada:
            #se uma das letras tentadas estiver na palavra, add, senao, add um '_'
            if letra not in self.letras_tentadas:
                palavra_escondida+='_'
            else:
                palavra_escondida+=letra
        return palavra_escondida
    
    def game_status(self):
        pass

#start

#cria objeto Hangman
fc1 = Hangman(input('Oi, bem-vindo(a), insira seu nome: '))
print(fc1.get_nome())
while not fc1.check_win():
    limpa_tela()

    #print game stts
    fc1.game_status()
    #captura caractere do user e verifica se ta certo
    fc1.tentativa(input('\nDigite uma letra ->'))
