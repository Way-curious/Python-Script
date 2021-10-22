theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
turn = 'X'
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
def checkBoard(board1,turn): 
        if (board1['1']==board1['2'] and board1['1'] == board1['3'] ):
            if (board1['1'] != ' ' and board1['2'] != ' ' and board1['3'] != ' '):
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                print ('the winner is',turn)
                exit()    
        elif (board1['4']==board1['5'] and board1['4'] == board1['6']):
            if (board1['4'] != ' ' and board1['5'] != ' ' and board1['6'] != ' '):
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                print ('the winner is',turn)
                exit()
        elif (board1['7']==board1['8'] and board1['7'] == board1['9']):
            if (board1['7'] != ' ' and board1['8'] != ' ' and board1['9'] != ' '):
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                print ('the winner is',turn)
                exit() 
        elif (board1['1']==board1['4'] and board1['1'] == board1['7']):
            if (board1['1'] != ' ' and board1['4'] != ' ' and board1['7'] != ' '):
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                print ('the winner is',turn)
                exit() 
        elif (board1['2']==board1['5'] and board1['2'] == board1['8']):
            if (board1['2'] != ' ' and board1['5'] != ' ' and board1['8'] != ' '):
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                print ('the winner is',turn)
                exit() 
        elif (board1['3']==board1['6'] and board1['3'] == board1['9']):
            if (board1['3'] != ' ' and board1['6'] != ' ' and board1['9'] != ' '):
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                print ('the winner is',turn)
                exit()  

for i in range(9):
    printBoard(theBoard)
    checkBoard(theBoard,turn)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)