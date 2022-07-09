##jogo da forca

#import
import random

print('BEM VINDE AO JOGO DA FORCA\n\n')

##criando o tabuleiro
tabuleiro= [
    '''
    >>>>>>>>>Hangman<<<<<<<< 
    +---+
    |   |
        |
        |
        |
    ========''', '''
    +---+
    |   |
    O   |
        |
        |
    ========''', '''
    +---+
    |   |
    O   |
    |   |
        |
    ========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
    ========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
    ========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
    ========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
    ========'''
]

#criação de classe

class Hangman():
    #método construtor

    def __init__(self, word):
        self.word = word
        self.guessed = []
        self.wrong = []


    #método de adivinhar palavra
    def guess(self, letter):
        self.letter = letter
        if self.letter in self.word and self.letter not in self.guessed:
            self.guessed.append(letter)
        elif self.letter not in self.word and self.letter not in self.wrong:
            self.wrong.append(letter)
        else:
            return False
        return True


    #método para determinar se o jogo acabou
    def hang_over(self):
        return self.hang_won() or (len(self.wrong) == 6)


    #método para determinar se o jogador venceu
    def hang_won(self):
        if '_' not in self.hide_word():
            return True
        else:
            return False


    #método para ocultar letras no board
    def hide_word(self):
        resp = ''

        for letter in self.word:
            if letter not in self.guessed:
                resp += '_'
            else:
                resp += letter

        return resp



    #método para atualizar as letras no board
    def print_status(self):
        print(tabuleiro[len(self.wrong)])
        print('Palavra: ', self.hide_word())

        print('Erros:')
        for letter in self.wrong:
            print(letter,)






#função para escolher uma palavra aleatória
def rand_word():
    with open("index.txt", "rt") as f:
        bank = f.readlines()
        #ignorando os espaços em branco
        return bank[random.randint(0, len(bank))].strip()

#execução do programa
def main():
    #objeto
    game = Hangman(rand_word())

    while not game.hang_over():
        game.print_status()
        user_input = input('Digite uma letra: ')
        game.guess(user_input)

    # Verifica o status do jogo
    game.print_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hang_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)




# Executa o programa
if __name__ == "__main__":
    main()




