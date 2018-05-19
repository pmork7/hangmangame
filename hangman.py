import random

fhandle = open('wordlist.txt', 'r')
wordlist = []

for word in fhandle:
    word = word.rstrip()
    wordlist.append(word)


rand = random.randint(0,len(wordlist) - 1)

guessword = wordlist[rand]
answerblock = []
for letter in guessword:
    answerblock.append(' _ ')

#print(guessword)

def findIndexOf(letter, word):
    index = []
    for i in range(0, len(word)):
        if word[i] == letter:
            index.append(i)
    return index

def contains(letter, word):
    for l in word:
        if l == letter:
            return True
    return False

def checkGuesses(letter, guesslist):
    for l in guesslist:
        if letter == l:
            print('You already guessed that letter.')
    guesslist.append(letter)

def bodyPartPrinter(n):
    if n == 0:
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('                       ')
        print('_______________________')
        print()
    elif n == 1:
        print('                        ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('___________________|____')
        print()
    elif n == 2:
        print('   |_________________                 ')
        print('   |               |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('___________________|____')
        print()
    elif n == 3:
        print('   |_________________                 ')
        print('   |     |         |    ')
        print('         |         |    ')
        print('         |         |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('___________________|____')
        print()
    elif n == 4:
        print('   |_________________                 ')
        print('   |     |         |    ')
        print('         |         |    ')
        print('         |         |    ')
        print('        ***        |    ')
        print('       *   *       |    ')
        print('        ***        |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('___________________|____')
        print()
    elif n == 5:
        print('   |_________________                 ')
        print('   |     |         |    ')
        print('         |         |    ')
        print('         |         |    ')
        print('        ***        |    ')
        print('       *   *       |    ')
        print('        ***        |    ')
        print('         *         |    ')
        print('         *         |    ')
        print('                   |    ')
        print('                   |    ')
        print('                   |    ')
        print('___________________|____')
        print()
    elif n == 6:
        print('   |_________________                 ')
        print('   |     |         |    ')
        print('         |         |    ')
        print('         |         |    ')
        print('        ***        |    ')
        print('       *   *       |    ')
        print('        ***        |    ')
        print('         *         |    ')
        print('        ***        |    ')
        print('       *   *       |    ')
        print('                   |    ')
        print('                   |    ')
        print('___________________|____')
        print()
    else:
        print('   |_________________                 ')
        print('   |     |         |    ')
        print('         |         |    ')
        print('         |         |    ')
        print('        ***        |    ')
        print('       *x x*       |    ')
        print('        ***        |    ')
        print('         *         |    ')
        print('        ***        |    ')
        print('       * * *       |    ')
        print('        * *        |    ')
        print('       *   *       |    ')
        print('___________________|____')
        print()


print('Welcome to Hangman!')
print()
print('Do yer best to guess the word or yer partner shall perish.')
print()
print('***********************************************************')
guesses = 0
lettersfound = 0
guessedLetters = []
while lettersfound < len(guessword) and guesses < 7:
    bodyPartPrinter(guesses)
    print()
    print('The word has this many spaces left...')
    print()
    for i in answerblock:
        print(i, end = ' ')
    print()
    print()
    guess = input('Guess a letter in the word - ')
    if len(guessedLetters) < 1:
        guessedLetters.append(guess)
    checkGuesses(guess, guessedLetters)
    print()
    if contains(guess, guessword):
        print('Correct!')
        print()
        matches = findIndexOf(guess, guessword)
        for num in matches:
            answerblock[num] = guessword[num]
            lettersfound += 1 
    else:
        print('Wrong!')
        print()
        guesses += 1
    if guess == '!':
        break

if lettersfound < len(guessword):
    print('Alas, you have failed...')
    print('The word was \'{:s}\'.'.format(guessword))
else:
    for i in answerblock:
        print(i, end = ' ')
    print('Hooray! You have saved your partner by guessing the word \'{:s}\'.'.format(guessword))
