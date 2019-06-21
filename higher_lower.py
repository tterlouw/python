# imported libraries
import random

# global variables
game_on = True
guesses = None
secret = None

# function for easy version
def difficulty_level_easy():
    global secret
    global game_on
    secret = int(random.randrange(0,1000))
    while game_on == True:
        guess = int(input('Guess a number: '))
        if guess > secret:
            print('You Guessed to high, try again')
        elif guess < secret:
            print('The guessed to low, try again')
        elif guess == secret:
            print('You guessed right, you win!')
            play_again()

# function for hard version
def difficulty_level_hard():
    global secret
    global game_on
    secret = int(random.randrange(0,1000))
    guesses = 3
    for i in range(guesses):
        guess = int(input('Guess a number. '))
        if i == 2:
            print('Game over. Too many guesses. The number is ' + str(secret))
            play_again()
        elif guess > secret:
            print('your guess is too high. Try again.')
        elif guess < secret:
            print('your guess is too low. Try again.')
        elif guess == secret:
            print('You win!')
            play_again()

# function to start game
def start_game():
    global game_on
    game_on = True
    level = input('Wich game difficulty to you want to play? Easy, Hard or do you want to quit? ')
    if level == 'Easy':
        difficulty_level_easy()
    elif level == 'Hard':
        difficulty_level_hard()
    elif level == 'quit':
        game_on = False
    else:
        print('Wrong choice, please try again')
        play_again()

def play_again():
    global game_on
    play = input('Play again? Yes or No. ')
    if play == 'Yes':
        start_game()
    elif play == 'No':
        print('Thanks for playing. Bye')
        game_on = False
    else:
        game_on = False

# function to stop game
def quit():
    while game_on == False:
        print('Thank you for playing, Bye!')
        exit()

# function calls
start_game()
quit()

