import random

keepPlaying = True

number = random.randint(1,9)

while keepPlaying:
    while True:
        try:
            userGuess = int(input('Enter your guess: '))
        except Exception:
            print("wrong input")
        else:
            break
    
    if userGuess < number:
        print("you guessed too low")
    elif userGuess == number:
        print("you made the right guess")
        break
    else:
        print("you guessed too high")

    
    while True:
        try:
            reply = str(raw_input('would you like to try again? (y/n): ')).lower().strip()
            if reply[0] == 'y':
                keepPlaying = True
            if reply[0] == 'n':
                keepPlaying = False
        except Exception as err:
            print("wrong input: {}".format(err))
        else:
            break


print("thank you for guessing with us! good night")