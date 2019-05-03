import random
words = ['venom', 'carnage', 'riot', 'scream', 'phage', 'lasher', 'agony', 'scorn', 'raze', 'mania', 'maniac', 'toxin', 'antivenom', 'hybrid', 'knull', 'krobaa', 'sleeper']
lives_remaining = 8
guessed_letters = ''
def pick_a_word():
    word_position = random.randint(0, len(words) - 1)
    return words[word_position]
#print(pick_a_word())

def play():
    word = pick_a_word()
    print('Welcome to Hangman! The theme is the names of Symbiote characters in the Marvel Universe.')
    print('You have ' + str(lives_remaining) + ' guesses. Use them wisely!')
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win! Well Done!')
            break
        if lives_remaining == 0:
            print('For your lack of knowledge, you have been hanged by the neck until dead.')
            print('The character was: ' + word)
            break

def pick_a_word():
    word_position = random.randint(0, len(words) - 1)
    return words[word_position]

def get_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining: ' + str(lives_remaining))
    guess = input('Guess a letter or the whole name: ')
    return guess

def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            # letter matches
            display_word = display_word + letter
        else:
            # letter does not match
            display_word = display_word + '-'
    print(display_word)


def process_guess(guess, word):
    if len(guess) > 1 and len(guess) == len(word):
        #guess entire word
        return whole_word_guess(guess, word)
    else:
        #guess one letter
        return single_letter_guess(guess, word)

def whole_word_guess(guess, word):
    global lives_remaining
    if guess.lower() == word.lower():
        #if correct
        return word
    else:
        #if false
        lives_remaining = lives_remaining + -1
        return False

def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        # letter guess was incorrect
        lives_remaining = lives_remaining + -1
    guessed_letters = guessed_letters + guess.lower()
    if all_letters_guessed(word):
        #if you guess all the letters in the word you win
        return True
    #if guess is wrong
    return False

def all_letters_guessed(word):
    for letter in word:
        #if all letters are not guessed
        if guessed_letters.find(letter.lower()) == -1:
            return False
    #if all letters are guessed
    return True

#inititialize the game
play()
