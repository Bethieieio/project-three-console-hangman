from curses.ascii import isalpha
import random
from words import word_list

#fetches random word from words.py and returns it in capital letters
def get_word():
    word = random.choice(word_list)
    return word.upper()

#displaying word for each turn

#displaying word for each turn, will run until user guesses word or runs out of tries
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
        
        elif len(guess) == len(word) and guess.isalpha():
        
        else:
            print("Woops! Please enter a letter or word! :)")
        print(display_hangman(tries)
        print(word_completion)
        print("/n")