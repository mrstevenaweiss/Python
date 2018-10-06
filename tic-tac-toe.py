
theBoard = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
    }


winningCombos = [(1, 2, 3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

# def iCanWin:
# def opponentCanWin:

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def tileChecker(move):
    return theBoard[move] == ' '

def main():
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print("Turn for: " + turn + ". Move on which space? (use number 1-9)" )
        move = input()

        if tileChecker(move):
            print('also working')
        else:
            print('Choose another tile' '\n')



        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    print('The Game is Over')

main()

# def endGame()
