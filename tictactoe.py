import math


def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_winner(board, player):
   
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def make_move(board, move, player):
    board[move[0]][move[1]] = player

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            make_move(board, move, 'O')
            eval = minimax(board, depth + 1, False, alpha, beta)
            make_move(board, move, ' ')
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            make_move(board, move, 'X')
            eval = minimax(board, depth + 1, True, alpha, beta)
            make_move(board, move, ' ')
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_eval = -math.inf
    best_move = None
    for move in get_available_moves(board):
        make_move(board, move, 'O')
        eval = minimax(board, 0, False, -math.inf, math.inf)
        make_move(board, move, ' ')
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def play_game():
    board = create_board()
    current_player = 'X'
    
    while True:
        print_board(board)
        if current_player == 'X':
            move = tuple(map(int, input("Enter your move (row and column): ").split()))
            if move not in get_available_moves(board):
                print("Invalid move. Try again.")
                continue
        else:
            move = get_best_move(board)
        
        make_move(board, move, current_player)
        
        if is_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

play_game()