
"""
functionalities to implement:
-- print the board to the console
-- handle player moves && update board
-- check for a win
-- check for a tie
-- main game loop
"""

def print_board(board):
    print("")
    for i in range(3):
        for j in range(3):
            if board[i][j]=="":
                item=i*3+j+1
            else:
                item=board[i][j]
            print(item,"| ",end="")
        print("\b\b \n----------")
    print("")
    

def is_handled(board,player):
    try:
        move=int(input(f"Player {player}: "))
    except ValueError:
        print("Please enter a number!!")
        return False
    
    if move<1 or move>9:
        print("Please enter a number in the range 1:9")
        return False

    i=(move-1)//3
    j=(move-1)%3
    if board[i][j]=="":
        board[i][j]=player
        return True
    
    else:
        print("This square is already taken")
        return False


def is_winner(board,player):
    for i in range(3):
        row_count=column_count=0
        for j in range(3):
            if board[i][j]==player:
                row_count+=1
            if board[j][i]==player:
                column_count+=1
        if row_count==3 or column_count==3:
            print(f"Player {player} wins!!")
            return True
    
    l_diagonal=r_diagonal=0
    for i in range(3):
        if board[i][i]==player:
            l_diagonal+=1
        if board[i][2-i]==player:
            r_diagonal+=1
    if l_diagonal==3 or r_diagonal==3:
        print(f"Player {player} wins!!")
        return True
    
    return False


def is_tie(board):
    count=0
    for i in range(3):
        for j in range(3):
            if board[i][j]=="":
                return False
    
    print("Oops!! game terminated with a tie!!")
    return True


def main_game():
    board=[["","",""],["","",""],["","",""]]    

    player=input("Choose which symbol you want 'X' or 'Y', your oponent will take the other: ").lower()

    while player!='x' and player!='y':
        player=input("Please enter a valid symbol: ")
    
    if player=='x':
        oponent='y'
    else:
        oponent='x'

    print("To choose a specific square enter its number as follows:")
    print_board(board)

    while True:
        while not is_handled(board,player):
            pass
        
        print_board(board)

        if is_tie(board):
            break

        if is_winner(board,player):
            break
        
        if is_tie(board):
            break

        while not is_handled(board,oponent):
            pass

        print_board(board)

        if is_winner(board,oponent):
            break


if __name__=="__main__":
    main_game()