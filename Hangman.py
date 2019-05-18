while True:
    import random
    words = ['spiderman', 'venom', 'carnage', 'riot', 'scream', 'phage', 'lasher', 'agony', 'scorn', 'raze', 'mania', 'maniac', 'toxin', 'antivenom', 'hybrid', 'knull', 'krobaa', 'sleeper']
    lives_remaining = 7
    guessed_letters = ''
    def pick_a_word():
        word_position = random.randint(0, len(words) - 1)
        return words[word_position]
    #print(pick_a_word())

    #main method
    def play():
        word = pick_a_word()
        print('Welcome to Hangman! The theme is the names of Symbiote characters in the Marvel Universe.')
        print('You have ' + str(lives_remaining) + ' guesses. Use them wisely!')
        hanging_man_grafx(7)
        while True:
            guess = get_guess(word)
            hanging_man_grafx(lives_remaining-1)
            if process_guess(guess, word):
                print('You win! Well Done!\nYou had ' + str(lives_remaining) + ' lives to spare.')
                rank(lives_remaining)
                break
            if lives_remaining == 0:
                print('For your lack of knowledge, you have been hanged by the neck until dead.')
                rank(0)
                print('The character was: ' + word)
                break

    #chooses a word from the word bank
    def pick_a_word():
        word_position = random.randint(0, len(words) - 1)
        return words[word_position]

    #gets input for a guess
    def get_guess(word):
        print_word_with_blanks(word)
        print('Lives Remaining: ' + str(lives_remaining))
        guess = input('Guess a letter or the whole name: ')
        return guess

    #shows letters when guessed correctly
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

    #shows game progress with a graphic
    def hanging_man_grafx(lives_remaining) :
        if lives_remaining == 7:
            print('____\n|\n|\n|\n|\n|')
        if lives_remaining == 6:
            print('____\n|   |\n|\n|\n|\n|')
        if lives_remaining == 5:
            print('____\n|   |\n|   0\n|\n|\n|')
        if lives_remaining == 4:
            print('____\n|   |\n|   0\n|   |\n|\n|')
        if lives_remaining == 3:
            print('____\n|   |\n|   0\n|  -|\n|\n|')
        if lives_remaining == 2:
            print('____\n|   |\n|   0\n|  -|-\n|\n|')
        if lives_remaining == 1:
            print('____\n|   |\n|   0\n|  -|-\n|   |\n|')
        if lives_remaining == 0:
            print('____\n|   |\n|   0\n|  -|-\n|  /|\n|')

    #compare guess to answer
    def process_guess(guess, word):
        if len(guess) > 1 and len(guess) == len(word):
            #guess entire word
            return whole_word_guess(guess, word)
        else:
            #guess one letter
            return single_letter_guess(guess, word)

    #compare entire word guess to answer
    def whole_word_guess(guess, word):
        global lives_remaining
        if guess.lower() == word.lower():
            #if correct
            return word
        else:
            #if false
            lives_remaining = lives_remaining + -1
            hanging_man_grafx(lives_remaining)
            return False
    
    #keeps track with gloabal values
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

    #special case if all letters are guessed progressively
    def all_letters_guessed(word):
        for letter in word:
            #if all letters are not guessed
            if guessed_letters.find(letter.lower()) == -1:
                return False
        #if all letters are guessed
        return True

    #give a title based on performance
    def rank(lives_remaining):
        if lives_remaining == 7:
            print('You are a perfect host.')
        if lives_remaining == 6:
            print('You are an excellent host.')
        if lives_remaining == 5:
            print('You are a great host.')
        if lives_remaining == 4:
            print('You are a suitable host.')
        if lives_remaining == 3:
            print('You are a poor host.')
        if lives_remaining == 2:
            print('You are a temporary host.')
        if lives_remaining == 1:
            print('You are just fuel in the tank.')


    #inititialize the game
    play()

    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input. Enter y to continue or n to terminate.')
    if answer == 'y':
        continue
    else:
        print('Thank you for playing.')
        break
