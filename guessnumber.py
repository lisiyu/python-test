#This is a guess the number game
import random
secretNumber = random.randint (1,20)
print('I am thinking of a number betwen 1 and 20.')

# Ask the player to guess 6 times
for guesscishu in range(1,7):
        print('Take a guess.')
        #try:
        guessNo = int(input())
        #except:
        print('你输入的不是数字')
        #    continue
        if guessNo < secretNumber:
                print('Your guessNo is too low.')
        if guessNo > secretNumber:
                print('Your guessNo is too high.')
        else:
                break
if guessNo == secretNumber:
        print('Good job!Yuou guessed my number in ' + str(guesscishu) + ' guesses! ')
else:
        print('Nope.The number I was thinking of was' + str(secertNumber))

