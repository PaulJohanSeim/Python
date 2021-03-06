# Copyright Paul-Johan Seim
# 
# Hangman game
#

# -----------------------------------


import random
import string

WORDLIST_FILENAME = "C:/Python27/Programs/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    count=0
    for char in lettersGuessed:
        print char
        if char in secretWord:
            print char
            count+=1
           
    print count
    print len(secretWord)
    if count >0:
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    resString=''
    for char in secretWord:
        if char in lettersGuessed:
            resString= resString + ' ' + char + ' '
        else:
            resString= resString + ' ' + '_' + ' '
        
    return resString

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    resString=''
    alFa='abcdefghijklmnopqrstuvwxyz'
    for char in alFa:
        if char in lettersGuessed:
            resString=resString+''
        else:
            resString=resString+char
    
    return resString
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' +str(len(secretWord))+ ' letters long.')
    print('-------------')
    numGuesses=8
    print('You have '+str(numGuesses)+ ' guesses left.')
    print('Available letters: abcdefghijklmnopqrstuvwxyz')
    
    count=0
    z=''
    while True:
        z=z+str(raw_input("Please guess a letter: "))        #z+ component adds the previous value of z
        letterGuess = z.lower()
        print letterGuess
        guessString = getGuessedWord(secretWord, letterGuess)
        
        if isWordGuessed(secretWord, letterGuess) == True:
            print('Good Guess: '+str(guessString))
            count+=1
        elif isWordGuessed(secretWord, letterGuess) == False:
            print('Oops! That letter is not in my word')
        else:
            print('Oops! You''ve already guessed that letter:')
            
        if isWordGuessed(secretWord, letterGuess) == True and count==len(secretWord):
            break
        
        print('------------------------')
        numGuesses-=1
        if numGuesses==0:
            print('You ran out of guesses. The word was ' +str(secretWord))
            break
        print('You have ' +str(numGuesses)+ ' guesses left.')
        
        print('Available letters: ' +str(getAvailableLetters(letterGuess)))
    
    print('------------------------')
    print('Congratulations, you won!')
    return True






# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
