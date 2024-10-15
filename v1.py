from os import system, name
import random
from json import dumps

#limpa tela
def limpa_tela() -> None:
    #nt caso seja windows, senao entende-se que se trata de outro so
    _ = system('cls') if name == 'nt' else system('clear') 
    

#imprime a palavra recebida letra a letra com espacos
def imprime_palavra(p) -> None:
    for letra in p: print(f'{letra}', end=' ')


#substitui a impressao 
def preenche_palavra(letra_substituida: str, lista_underlines: str, palavra_referencia: str) -> bool:
    for k, l in enumerate(palavra_referencia):
        #SE NUMA DETERMINADA POSICAO A LETRA QUE EU QUISER TROCAR FOR A MESMA QUE A QUE ESTA PASSANDO, ENTAO REALIZA A TROCA NESTA PÓSICAO
        if l == letra_substituida:
            lista_underlines.remove(k)
            lista_underlines.insert(k, letra_substituida)


#inicia game
def game() -> None:
    #intro
    limpa_tela()
    print('Bem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')
    print('-'*20)

    #palavras que podem ser sorteadas
    palavras: str = dumps('words.json')

    #sorteio da palavra
    palavra_sorteada: str = random.choice(palavras)
    print(palavra_sorteada)
    #lista de acertos
    letras_acertadas = list()

    #a palavra sorteada tem um certo tamanho, então vamos cobrir a lista de letras acertadas de _ e a cada acerto trocamos pela letra certa
    for _ in  range(len(palavra_sorteada)):
        letras_acertadas.append('_')
    
    #cria lista vazia para armazenar letras adivinhadas
    letras_tentadas = list()

    #definindo qtd de tentativas
    chances: int = 6
    #variável para verificar se o jogador venceu
    win = False

    #enquanto nao acertar ou acabar as chances, segue
    for tentativas in range(chances, 0, -1):
        print(f'Chances: {tentativas}\nLetras erradas: {letras_tentadas}')
        entrada = input('Digite uma letra: ')
        
        if entrada in palavra_sorteada:
            win = preenche_palavra(entrada, letras_acertadas, palavra_sorteada)
            

        else:
            letras_tentadas.append(entrada)



#run
game()
