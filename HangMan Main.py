import random
from Words import word_list as wl

def get_word():
    word = random.choice(wl)
    return word.lower()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(hangman_display(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter!", guess)
            elif guess not in guessed_letters:
                print("Letter is not in the word", guess)
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess,  "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess!")
        print(hangman_display(tries))
        print(word_cpmpletion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("L bozo, try harder next time. The word is " + word)


def hangman_display(tries):
    HANGMAN_PICS = ['''
         +---+
             |
             |
             |
            ===''', '''
         +---+
         O   |
            |
            |
           ===''', '''
        +---+
        O   |
        |   |
            |
           ===''', '''
        +---+
        O   |
       /|   |
            |
           ===''', '''
        +---+
        O   |
       /|\  |
            |
           ===''', '''
        +---+
        O   |
       /|\  |
       /    |
           ===''', '''
        +---+
        O   |
       /|\  |
       / \  |
           ===''']

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__=="__main__":
    main()