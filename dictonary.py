import random

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def gameStatus():
    return 1

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


print('Lets play the game!')
print('Doing Toss between player x turn and player o')

players =['x','o']

def toss():
    global players
    return(random.randint(0,1))

turn =players[toss()]
print(turn + ' won the toss!')
printBoard(theBoard)

print('Where do you want to put ' + turn)

game_status=1
while game_status!=0:
    print('Where do you want to put ' + turn)
    place = input()
    if place not in theBoard.keys():
        print('Enter correct place')
    else:
        if(theBoard[place] == ' '):
            theBoard[place]=turn
            if (turn=='x'):
                turn = 'o'
            else:
                turn = 'x'
        else:
            print('Place already filled. Choose another position.')
    game_status = gameStatus()        
    printBoard(theBoard)
