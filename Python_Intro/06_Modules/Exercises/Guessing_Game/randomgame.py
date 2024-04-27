import sys
import random

def main():
    _MIN = int(sys.argv[1])
    _MAX = int(sys.argv[2])

    num_to_guess = random.randint(_MIN, _MAX)
    userGuess = None
    amount_of_guess = 0

    while(userGuess != num_to_guess):
        try:
            userGuess = int(input(f'Enter a number from {_MIN} to {_MAX}: '))

        except (TypeError, ValueError):
            print(f'Not a number. Try again')
            continue

        if(userGuess == num_to_guess):
            print(f'Correct! You did it in {amount_of_guess} tries!')

        if(userGuess > num_to_guess):
            print(f'Incorrect. Too high.')
        else:
            print(f'Incorrect. Too low.')
        amount_of_guess += 1

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage Error: python3 randomgame.py <min> <max>')
    else:
        main()
    

