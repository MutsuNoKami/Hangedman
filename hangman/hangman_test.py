import random
from typing_extensions import Self

class Hangman:


    def __init__(self, word_list, num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # 2. {word_guessed}
  
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice((word_list))
        self.num_letters = len(self.word)
        self.used_letter = []
        self.list_letters = []
        self.word_guessed = "_" * len(self.word)
        
        num_lives=5
        print(f"The mystery word has {len(self.word)} characters")
        print(self.word_guessed)
        print(num_lives)
        pass

    def check_letter(self, letter,) -> None:
        '''
        
        '''
        letter = letter.lower()
        if letter in self.word:
            print("correct")
            
            for i in range(0, len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] += letter
                    print(f"{letter}", end="")
                    self.num_letters -= 1
                
        else:
            self.num_lives -= 1
                
        self.word_guessed.append[letter]
        letter = self.letter
        pass

    def ask_letter(self):
        
    
        print('Enter a letter')
        self.letter = input()
        letter = self.letter.lower()
        used_letter = self.used_letter
        
        if len(letter) != 1:
            print("Please, enter just one character")
        elif letter in used_letter:
            print("This letter has been guessed.")
        elif letter not in "qwertyuiopasdfghjklzxcvbnm":
            print("Please, enter a letter")
        else:
            Hangman.check_letter(self, letter)
        
    pass

def play_game(word_list):
    
    game = Hangman(word_list, num_lives=5)
   
    while True:
        if game.num_lives > 0 and game.num_letters > 0:
            game.ask_letter()
            if "_" not in game.word_guessed:
                print("Congratulations, you won!")
                exit()
            elif game.num_lives <= 0:
                print (f"You ran out of lives. The word was {game.word}")
            break
        

    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
