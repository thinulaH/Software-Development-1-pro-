import random
hidden = random.randint(1,20)

guess = int(input('Enter a guess (between 1 and 20) :'))
while (guess!=hidden) :
    print(guess,' is not correct')
    if(guess<hidden):
        print('Guessed number is too low')
    elif (guess>hidden):
        print('Guessed number is too high')
    guess = int(input('Enter a guess :'))
print(guess,"is correct")
