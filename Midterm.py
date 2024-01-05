"""
Create a Python file named Midterm-Q2.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

"""


import random

def choose_word():
    """
    Choose a random word from the array of words.
    """
    #These are the words to choose from
    words = ['python', 'programming', 'challenge', 'random', 'hidden']
    return random.choice(words)

def display_word(word, guessed_letters):
    """
    Display the word with hidden letters.
    """
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def get_guess():
    """
    Get a valid single-letter guess from the user.
    """
    while True:
        guess = input("Enter a single letter: ").lower()
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print("Invalid input. Please enter a single letter.")

def play_game():
    """
    Main function to play the word guessing game.
    """
    word_to_guess = choose_word()
    guessed_letters = []
    max_attempts = 6
    attempts_left = max_attempts

    print("Welcome to the Word Guessing Game!")
    print(display_word(word_to_guess, guessed_letters))

    while '_' in display_word(word_to_guess, guessed_letters) and attempts_left > 0:
        print(f"Attempts left: {attempts_left}")
        guess = get_guess()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)
#This will appear when ever you guess a letter, and depending on if it is correct or not one of these messages will apear
        if guess not in word_to_guess:
            attempts_left -= 1
            print("Incorrect guess. Try again.")
        else:
            print("Correct guess!")

        print(display_word(word_to_guess, guessed_letters))

#if you get the word correct then this message will pop up meaing that you have wone the game
    if '_' not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You guessed the word. You Won!!!!!")
        #if you get the word wrong and run out of your six lives then this message will pop up and give you the aswer that it was looking for
    else:
        print(f"Sorry, you're out of attempts. The word was {word_to_guess}.YOU LOSER!!!!!!")

if __name__ == "__main__":
    play_game()