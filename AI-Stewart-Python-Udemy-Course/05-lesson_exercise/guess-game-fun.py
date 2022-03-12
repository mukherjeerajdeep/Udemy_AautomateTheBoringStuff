import random

print('Please tell you name : ')
playerName = input()

print('Welcome, ' + playerName + ', to the guess game ')

secretNumber = random.randint(1, 20)

# print('The secret number is : ' + str(secretNumber))

attempt = 0  # Someone can regulate it from here
maxTry = 5

while attempt < maxTry:
    print('Please guess a number between 1 to 20')

    try:
        guess = int(input())
        if guess > secretNumber:
            print('Your guess is too high')
        elif guess < secretNumber:
            print('Your guess is too low')
        else:  # guess and secret matched
            break
    except ValueError:
        print('Please enter a valid number between 1-20')
    attempt += 1
    print('Attempt left : ' + str(maxTry - attempt))

if secretNumber != guess:
    print('You maxed out your retry, the secretNumber was ' + str(secretNumber))
else:
    print('You guessed correctly, the secretNumber was ' + str(secretNumber))
