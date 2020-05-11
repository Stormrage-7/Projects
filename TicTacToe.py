import random

l=['   ','   ','   ',
  '   ','   ','   ',
  '   ','   ','   ']

# Initializing
def Initialize():
    global l
    print("TicTacToe\n")
    print("Press 1 : PvE AI still in Development :(")
    print("Press 2 : PvP\n")
    players=int(input())
    prtscr()



#Display Board
def prtscr():
    global l
    for i in range(len(l)):
        if i+1==9:
            print(l[i])
        elif (i+1)%3==0:
            print(l[i])
            print('---+---+---')
        else:
            print(l[i],end='|')

# Endgame Condition
def winning_condition():
    global winner
    global l
    # Lateral
    if l[0] == l[1] == l[2] != '   ':
        winner=l[0].strip()

    elif l[3] == l[4] == l[5] != '   ':
        winner=l[3].strip()

    elif l[6] == l[7] == l[8] != '   ':
        winner=l[6].strip()

    # Vertical
    elif l[0] == l[3] == l[6] != '   ':
        winner=l[0].strip()

    elif l[1] == l[4] == l[7] != '   ':
        winner=l[1].strip()

    elif l[2] == l[5] == l[8] != '   ':
        winner=l[2].strip()

    # Diagonal
    elif l[0] == l[4] == l[8] != '   ':
        winner=l[0].strip()

    elif l[2] == l[4] == l[6] != '   ':
        winner=l[2].strip()

    if winner!=0:
        return 1
    else:
        return 0



#Handling Turns
def Handle_Turn(turn):
    global l

    if turn%2==0:
        loc=input("Player 1:")
    else:
        loc=input("Player 2:")
    try:
        loc=int(loc)
        loc-=1
        x=l[loc]
    except:
        return 0

    if l[loc]!='   ':
        return 0
    else:
        if turn%2==0:
            l[loc]=' X '
        else:
            l[loc]=' O '
        prtscr()
        return 1


def Check():
    turn=0
    while (turn<9):

        x=Handle_Turn(turn)
        if x==0:
            continue
        else:
            turn+=1
        if winning_condition():
            break

n=int(input("Times: "))
for i in range(n):
    l=['   ','   ','   ',
      '   ','   ','   ',
      '   ','   ','   ']
    winner=0
    Initialize()
    Check()

    print("Winner is",winner)
    print()
