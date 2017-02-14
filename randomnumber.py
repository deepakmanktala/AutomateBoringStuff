import random

secretNumber=random.randint(1,50)
print(secretNumber)
print('PLease guess a number between 1 to 50' )
for i in range(1,21):
    guessnumber=int(input())
    if guessnumber > secretNumber:
        print('You are high')
    if guessnumber < secretNumber:
        print('You are low')
    if guessnumber==secretNumber:
        print('you have guessed correct number')
        break    

else:
    print('sorry better luck next time')
    
