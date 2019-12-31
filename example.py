import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1,100)
print('Hello ' + name + ', do you want to play a game?')
game = input('Y or N: ')
if game != "Y":
    print("But you're already here. I'm thinking of a number between 1 and 100.")
else:
    print("I'm thinking of a number between 1 and 100.")

# Ask the player to guess 6 times
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())
      
    if guess < secretNumber:
            print("Uh uh uh. Too low.")
    elif guess > secretNumber:
            print('Oh no. Too high')
    else:
        break
    if guessesTaken < 5:
        print('You have ' + str(6 - guessesTaken) + ' guesses left. Think harder!')
    elif guessesTaken == 5:
        print('You have 1 guess left. Make it count.')
    else:
        break
if guess == secretNumber:
    print('Well done, ' + name + ', the number was ' + str(secretNumber)+'. You have saved yourself this time. Goodbye')
else:
    print('You have not done well today, the number I was looking for is ' +str(secretNumber) + 'and for that you will perish.')
