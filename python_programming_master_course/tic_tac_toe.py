def printing_board(board):
    """
    This function is supposed to print the board content.
    It takes the board as an input and prints the board as an output.
    """
    for row in board:
        print(row[0],"|",row[1],"|",row[2])
        print("---------")


def handling_input(user_name,board):
    """
    This function is supposed to handle any errors when player does something unexpected.
    It returns False if something went wrong.
    It return True if everything is alright and the user has successfully reserved a valid square.
    """
    user_symbol=input("Enter your symbol, 'x' or 'o': ")
    user_symbol=user_symbol.strip().lower()

    if not(user_symbol=="x" or user_symbol=="o"):
        print("Please enter a correct symbol!!")
        return False
    
    if user_symbol!=user_name:
        print("This is not your turn!!")
        return False
    
    try:
        user_input=int(input("Enter the number of square: "))
    except ValueError:
        print("Please, make sure you 've entered a number!!")
        return False
    
    if user_input<1 or user_input>9:
        print("Please, make sure the number is in the correct range!!")
        return False

    row=(user_input-1)//3
    column=(user_input-1)%3
    if board[row][column]!=" ":
        print("This location is already taken")
        return user_input
    else:
        board[row][column]=user_name
        return True


def check_for_win(user_name,board):
    """
    This functions sweeps the board for a win.
    It takes the user symbol which we are checking for his winning and the board as inputs.
    It returns 'True' for a winning and 'False' for a loss.
    """
    # checking for a row or a column with three matching symbols:
    i=0
    while i<3:
        row_count=column_count=0
        j=0
        while j<3:
            if board[i][j]==user_name:
                row_count+=1
            if board[j][i]==user_name:
                column_count+=1
            j+=1
        if row_count==3 or column_count==3:
            return True
        i+=1
    
    # checking for a diagnol with three mathcing symbols:
    r_diagonal=l_diagonal=0
    for i in range(3):
        if board[i][i]==user_name:
            r_diagonal+=1
        if board[i][2-i]==user_name:
            l_diagonal+=1
    if r_diagonal==3 or l_diagonal==3:
        return True
    else:
        return False


def check_for_tie(board):
    """
    This function checks whether all the board squares are taken or not.
    It takes the board as an input and return whether all the squares are taken 'True' or not 'False'.
    """
    for row in board:
        for square in row:
            if square==" ":
                return False
    return True
        

def main_game():
    """
    This is the main fuction which combines all other sub-routines in a one unit to:
    1. print the board content
    2. handle the user input
    3. checking for a winner
    4. checking for a draw
    """
    print()
    print("First player always takes the symbol: 'x' and the second takes 'o'.")
    print("To select a specific square, enter a number in the range: 1-9 which corresponds to that square:")
    board=[["1","2","3"],["4","5","6"],["7","8","9"]]
    printing_board(board)
    board=[[" "," "," "],[" "," "," "],[" "," "," "]]
    while True:
        
        while True: 
            if handling_input('x',board):
                break

        printing_board(board)
        if check_for_win('x',board):
            print("Player 'x' wons!!!")
            break

        while True:
            if handling_input('o',board):
                break

        printing_board(board)
        if check_for_win('o',board):
            print("Player 'o' wins !!!")
            break

        if check_for_tie(board):
            print("Game terminated with a draw!!!")
            break


main_game()
