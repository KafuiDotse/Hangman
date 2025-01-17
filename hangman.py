# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if letters_guessed[-1] in secret_word:
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    x=""
    for i in secret_word:
        if i in letters_guessed:
            x+=i
        else:
            x+="_ "
    return x



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = "qwertyuiopasdfghjklzxcvbnm"
    new_available_letters=""
    for i in available_letters:
        if i in letters_guessed:
            pass
        else:
            new_available_letters+=i
    return new_available_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings=3
    guesses=6
    letters_guessed=[]
    print(f"""Loading word list from file...
55900 words loaded
Welcome to the game hangman.
I am thinking of a word that is {len(secret_word)} letters long""")
    
    while guesses>0 :
        if get_guessed_word(secret_word,letters_guessed)==secret_word:
            break
        print("-----------------------------")
        print(f"""You have {guesses} guesses left
You have {warnings} warnings left
Available Letters: {get_available_letters(letters_guessed)}""")
        letter=input("Please guess a letter: ").lower()

        if letter.isalpha():
            if letter in letters_guessed:
                if warnings>0:
                    warnings-=1
                    print(f"Oops! You've already guessed that letter. You have {warnings} warrings left: {get_guessed_word(secret_word,letters_guessed)}")
                else:
                    if letter in "qwrtypsdfghjklzxcvbnm":
                        guesses-=1
                    else:
                        guesses-=2
                    
            else:
                letters_guessed.append(letter)

                if is_word_guessed(secret_word,letters_guessed)==True:
                    print(f"Good guess: {get_guessed_word(secret_word,letters_guessed)}")
                else:
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word,letters_guessed)}")
                    guesses-=1
        else:
            if warnings>0:
                warnings-=1
                print(f"Oops! That is not a valid letter. You have {warnings} warrings left: {get_guessed_word(secret_word,letters_guessed)}")
            else:
                guesses-=1

    if get_guessed_word(secret_word,letters_guessed)==secret_word:
        print("Congratulations, you won!")
        print(f"Your total score for the game is: {guesses*len(secret_word)}")
    else:
        print(f"Sorry, you lost!\nThe word was {secret_word}")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)




if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
