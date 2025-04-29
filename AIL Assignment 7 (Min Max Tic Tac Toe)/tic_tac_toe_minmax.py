import random
import time

# Constants
EMPTY = ' '
HUMAN = 'X'
AI = 'O'

def print_board(board):
    """Print the current state of the board."""
    print("-------------")
    for i in range(3):
        print(f"| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |")
        print("-------------")

def init_board():
    """Initialize an empty board."""
    return [EMPTY for _ in range(9)]

def get_available_moves(board):
    """Return a list of available moves."""
    return [i for i, cell in enumerate(board) if cell == EMPTY]

def is_winner(board, player):
    """Check if the specified player has won."""
    # Check all winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_board_full(board):
    """Check if the board is full."""
    return EMPTY not in board

def game_over(board):
    """Check if the game is over."""
    return is_winner(board, HUMAN) or is_winner(board, AI) or is_board_full(board)

def get_board_score(board, depth):
    """Evaluate the board for the AI player."""
    if is_winner(board, AI):
        return 10 - depth  # Win: positive score, prefer quicker wins
    elif is_winner(board, HUMAN):
        return depth - 10  # Loss: negative score, prefer slower losses
    else:
        return 0  # Draw

def minimax(board, depth, is_maximizing):
    """
    Implementation of the minimax algorithm.
    Returns the best score possible from the current board state.
    """
    # Terminal states check
    if is_winner(board, AI):
        return 10 - depth
    if is_winner(board, HUMAN):
        return depth - 10
    if is_board_full(board):
        return 0
    
    available_moves = get_available_moves(board)
    
    if is_maximizing:
        # AI's turn (maximizing)
        best_score = float('-inf')
        for move in available_moves:
            board[move] = AI
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY  # Undo move
            best_score = max(score, best_score)
        return best_score
    else:
        # Human's turn (minimizing)
        best_score = float('inf')
        for move in available_moves:
            board[move] = HUMAN
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY  # Undo move
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    """Find the best move for the AI using minimax algorithm."""
    best_score = float('-inf')
    best_move = None
    available_moves = get_available_moves(board)
    
    for move in available_moves:
        board[move] = AI
        score = minimax(board, 0, False)
        board[move] = EMPTY  # Undo move
        
        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move

def get_human_move(board):
    """Get a valid move from the human player."""
    available_moves = get_available_moves(board)
    
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8:
                print("Invalid move! Please enter a number between 0-8.")
            elif move not in available_moves:
                print("That cell is already taken! Try again.")
            else:
                return move
        except ValueError:
            print("Please enter a valid number.")

def display_guide():
    """Display a guide showing cell numbers."""
    guide_board = list(range(9))
    print("\nCell numbers guide:")
    print_board(guide_board)
    print()

def main():
    """Main game function."""
    print("Welcome to Tic-Tac-Toe with Minimax!")
    print("You are 'X' and the AI is 'O'")
    display_guide()
    
    board = init_board()
    
    # Randomly decide who goes first
    current_player = random.choice([HUMAN, AI])
    print(f"{'You go' if current_player == HUMAN else 'AI goes'} first!")
    
    while not game_over(board):
        print_board(board)
        
        if current_player == HUMAN:
            print("Your turn...")
            move = get_human_move(board)
            board[move] = HUMAN
        else:
            print("AI is thinking...")
            time.sleep(0.5)  # Add a small delay for better UX
            move = get_best_move(board)
            board[move] = AI
            print(f"AI chose position {move}")
        
        # Switch players
        current_player = AI if current_player == HUMAN else HUMAN
    
    # Game over
    print_board(board)
    
    if is_winner(board, HUMAN):
        print("You win! Congratulations!")
    elif is_winner(board, AI):
        print("AI wins! Better luck next time.")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()