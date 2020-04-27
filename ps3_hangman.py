# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 23:04:07 2017

@author: Oyelson J
"""
# Hangman game

import random


WORDLIST_FILENAME = "words.txt"


def loadWords():
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


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are
            in lettersGuessed;
      False otherwise
      secretWord = 'apple'
      lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
            break
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            secretWord = secretWord.replace(letter, " _ ")
    return secretWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
      import string
      print(string.ascii_lowercase)
     Note that with the 'import string' the inbuilt string property
     'string.ascii_lowercase' gives all in alphabet in lower case
    '''
    rem_alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in lettersGuessed:
        if letter.lower() in rem_alphabet:
            rem_alphabet = rem_alphabet.replace(letter.lower(), "")
    return rem_alphabet


def addGuessNoRepeat(guess, lettersGuessed):
    if guess not in lettersGuessed:
        lettersGuessed.append(guess)


def isLetterInSecretWord(secretWord, guess):
    '''
      secretWord = 'apple'
      lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
      guessedWord = '_ pp_ e'
    '''
    for word in secretWord:
        if word == guess:
            return True
    return False


def isLetterAlreadyGuessed(lettersGuessed, guess):
    for word in lettersGuessed:
        if word == guess:
            return True
    return False


def isNotAlpha(guess):
    non_alpha = ""
    for word in guess:
        if not word.isalpha():
            non_alpha += word
            # add a comma if you haven't reached the end of guess
            if word != guess[-1]:
                non_alpha += ", "
    return non_alpha


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    keep_guessing = True
    guesses = 8
    mistakesMade = 0
    lettersGuessed = []
    error = ""

    while keep_guessing:
        print('----------------------------------------------------')
        print('You have', guesses, 'guesses left.')
        print('Available Letters:', getAvailableLetters(lettersGuessed))
        if error != "":
            print(error)

        guess = input("Please guess a letter: ")
        guessInLowerCase = guess.lower().replace(" ", "")
#        lettersGuessed.append(guessInLowerCase)
        moveOn = False
        while moveOn is False:
            if guessInLowerCase == "":
                error = "NOTE: You must enter a letter! Input was empty"
                moveOn = False
                break
            elif len(guessInLowerCase) > 1:
                error = "NOTE: You are allowed one entry! You have " +\
                        str(len(guessInLowerCase)) +\
                            "; Entry was " + str(guessInLowerCase)
                moveOn = False
                break
            elif guessInLowerCase.isalpha() is False:
                error = "NOTE: Only alphabets are allowed! " +\
                    isNotAlpha(guess) + " were found"
                moveOn = False
                break
            else:
                moveOn = True
        if moveOn is True:
            error = ''
            if isWordGuessed(secretWord, lettersGuessed) is False:
                if isLetterInSecretWord(secretWord, guessInLowerCase):
                    if isLetterInSecretWord(secretWord, guessInLowerCase)\
                            and not\
                            isLetterAlreadyGuessed(lettersGuessed, guessInLowerCase):
                        print('Good guess: ', end="")
                        addGuessNoRepeat(guessInLowerCase, lettersGuessed)
                        print(getGuessedWord(secretWord, lettersGuessed))
                        if isWordGuessed(secretWord, lettersGuessed):
                            print('------------------------------------------')
                            print('Congratulations, you won!')
                            keep_guessing = False
                            break
                        keep_guessing = True
                    elif isLetterInSecretWord(secretWord, guessInLowerCase)\
                            and \
                            isLetterAlreadyGuessed(lettersGuessed, guessInLowerCase):
                        print('Oops! You\'ve already guessed that letter: ', end="")
                        addGuessNoRepeat(guessInLowerCase, lettersGuessed)
                        print(getGuessedWord(secretWord, lettersGuessed))
                        keep_guessing = True
                elif not isLetterInSecretWord(secretWord, guessInLowerCase)\
                        and\
                        isLetterAlreadyGuessed(lettersGuessed, guessInLowerCase):
                    print('Oops! You\'ve already guessed that letter: ', end="")
                    addGuessNoRepeat(guessInLowerCase, lettersGuessed)
                    print(getGuessedWord(secretWord, lettersGuessed))
                    keep_guessing = True
                else:
                    print('Oops! That letter is not in my word: ', end="")
                    addGuessNoRepeat(guessInLowerCase, lettersGuessed)
                    print(getGuessedWord(secretWord, lettersGuessed))
                    guesses -= 1
                    mistakesMade += 1
                    if guesses < 1:
                        print('----------------------------------------------')
                        print('Sorry, you ran out of guesses. The word was ' +
                              secretWord + '.')
                        addGuessNoRepeat(guessInLowerCase, lettersGuessed)
                        print("All guesses are", lettersGuessed)
                        keep_guessing = False
                        break
                    else:
                        keep_guessing = True
            else:
                print('Good guess:', secretWord)
                print('-----------------------------------------------------')
                print('Congratulations, you won!')
                addGuessNoRepeat(guessInLowerCase, lettersGuessed)
                print("All guesses are", lettersGuessed)
                keep_guessing = False
                break


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
