# hangman
# --modules --
import random

# -- functions --
def read_words_from_file(file_name):
    """
    function definition
    :param file_name: string of the file name
    :returns: list of words from the file
    """
    file = open(file_name, "r")

    word_list = []
    end_file = False

    while not end_file:
        word = file.readline()

        if word == "": # end of file
            end_file = True
        else:
            word = word.strip("\n")
            word_list.append(word)
    file.close()

    return word_list

def select_secret_word(word_list):
    """_summary_

    Args:
        word_list (_type_): _description_

    Returns:
        _type_: _description_
    """
    word = random.choice(word_list)
    return word

def get_user_input(list_of_all_guesses):
    good_input = False
    while not good_input:
        guess = input("Guess a letter: > ")

        if guess in list_of_all_guesses:
            print("You've guessed that letter.")
        else:
            good_input = True
            list_of_all_guesses.append(guess)
    
    return guess, list_of_all_guesses

# main code
all_guesses = []
list_of_words = read_words_from_file("word_list.txt")
print(list_of_words)

secret_word = select_secret_word(list_of_words)
print(f'secret word is {secret_word}')

game_over = False
while not game_over:
    # input
    letter, all_guesses = get_user_input(all_guesses)
    print(letter)