import random


def welcome_user():
    """
    Lets username choose his name
    Has to be alphabets only
    Greets the username with his chosen name
    """

    username = None

    while True:

        username = input('Enter your name\n')   # Lets user write his name

        if not username.isalpha():  # Has to be alphabetic character
            print('Username must be alphabets only')
            continue
        else:
            print(f'welcome {username}')
            break


print('Welcome to Hangman')
welcome_user()


def get_valid_word(words):
    """
    Generates a random word from word.py
    The word will be generated capital letters
    """
    word = random.choice(words)  # randomly chooses word from the list
    return word.upper()     # Word come back capital letters