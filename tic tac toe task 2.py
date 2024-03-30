import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False


def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def ai_move(board):
    empty_cells = get_empty_cells(board)
    for i, j in empty_cells:
        board[i][j] = 'O'
        if check_winner(board, 'O'):
            return
        board[i][j] = ' '
    
    for i, j in empty_cells:
        board[i][j] = 'X'
        if check_winner(board, 'X'):
            board[i][j] = 'O'
            return
        board[i][j] = ' '
    
    i, j = random.choice(empty_cells)
    board[i][j] = 'O'

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row = int(input("Enter row number (1-3): ")) - 1
        col = int(input("Enter column number (1-3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = "X"
            if check_winner(board, "X"):
                print("Congratulations! You win!")
                break
            elif len(get_empty_cells(board)) == 0:
                print("It's a draw!")
                break
            ai_move(board)
            print_board(board)
            if check_winner(board, "O"):
                print("Sorry! You lose!")
                break
        else:
            print("That cell is already occupied. Try again.")

if __name__ == "__main__":
    main()