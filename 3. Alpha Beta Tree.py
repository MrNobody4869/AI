# Tic Tac Toe using Non-AI (Random) and AI (Minimax + Alpha-Beta) techniques

import math
import random

# Display the current game board in 3x3 format
def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print("\n")

# Check if there is a winner by evaluating all win combinations
def check_winner(board):
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    # Verify each winning pattern
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]  # Return the winning player symbol
    return None

# Check if no empty spaces remain
def is_full(board):
    return " " not in board

# ----------- NON-AI VERSION (Random CPU Moves) -----------

# Select a random valid move from available positions
def random_move(board):
    available = [i for i in range(9) if board[i] == " "]
    return random.choice(available) if available else -1

# Game loop for human vs random-move computer
def non_ai_game():
    board = [" "] * 9
    print("Welcome to Tic Tac Toe (Non-AI Version)")
    print("You are 'X' and Computer is 'O'")
    print_board(board)

    while True:
        # Human player's move input and validation
        try:
            pos = int(input("Enter your move (1-9): ")) - 1
            if pos < 0 or pos > 8 or board[pos] != " ":
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        board[pos] = "X"
        print_board(board)

        # Check game state after player's move
        if check_winner(board):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # Computer move is made randomly from empty positions
        print("Computer is playing (Non-AI random move)...")
        ai_pos = random_move(board)
        board[ai_pos] = "O"
        print_board(board)

        # Check game state after computer move
        if check_winner(board):
            print("Computer wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# ----------- AI VERSION (Minimax + Alpha-Beta Pruning) -----------

# Minimax: evaluates board recursively to choose optimal move
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)

    # Terminal state evaluations
    if winner == "O":
        return 1   # AI wins
    elif winner == "X":
        return -1  # Human wins
    elif is_full(board):
        return 0   # Draw

    # Maximizer branch (AI plays as 'O')
    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:  # Alpha-Beta pruning
                    break
        return max_eval
    
    # Minimizer branch (Human plays as 'X')
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:  # Alpha-Beta pruning
                    break
        return min_eval

# Compute the best possible move for AI using minimax
def best_move(board):
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = " "
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# Main AI gameplay loop
def ai_game():
    board = [" "] * 9
    print("Welcome to Tic Tac Toe (AI Version)")
    print("You are 'X' and AI is 'O'")
    print_board(board)

    while True:
        # Human move input
        try:
            pos = int(input("Enter your move (1-9): ")) - 1
            if pos < 0 or pos > 8 or board[pos] != " ":
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        board[pos] = "X"
        print_board(board)

        # Game state check after player move
        if check_winner(board):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI selects best move using minimax strategy
        print("AI is calculating optimal move...")
        ai_pos = best_move(board)
        board[ai_pos] = "O"
        print_board(board)

        # Game state check after AI move
        if check_winner(board):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Menu-driven game selector
def main():
    while True:
        print("\n--- TIC TAC TOE ---")
        print("1. Non-AI Version (Random Moves)")
        print("2. AI Version (Minimax with Alpha-Beta)")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            non_ai_game()
        elif choice == "2":
            ai_game()
        elif choice == "3":
            print("Exiting the game...")
            break
        else:
            print("Invalid choice! Please try again.")

# Program entry point
if __name__ == "__main__":
    main()




































# Viva Questions & Answers — Alpha-Beta Search

# 1. What is Alpha-Beta pruning?
#    An optimization of Minimax that removes branches which cannot affect the final decision.

# 2. Why is Alpha-Beta used?
#    To reduce the number of evaluated nodes and make game AI faster without changing the result.

# 3. Define Alpha and Beta.
#    Alpha = best value/max score the maximizing player can guarantee so far.
#    Beta = best value/min score the minimizing player can guarantee so far.

# 4. Does Alpha-Beta change the final output?
#    No — it only reduces computation. The result remains same as Minimax.

# 5. What triggers pruning?
#    When Beta <= Alpha, further nodes in that branch are skipped (no better outcome possible).

# 6. What type of algorithm is it?
#    Depth-First Search based adversarial search for two-player turn-based games.

# 7. Where is it used?
#    Games like Tic-Tac-Toe, Chess, Checkers, Connect-4, etc.

# 8. Time complexity benefit?
#    Minimax worst case: O(b^d). Alpha-Beta best case: O(b^(d/2)).

# 9. What are maximizing and minimizing players?
#    Maximizer tries to get highest score (AI), minimizer tries to reduce score (opponent).

# 10. What is a leaf node?
#     A terminal game state where no moves left (win/loss/draw state).

# 11. What is a heuristic function?
#     Evaluates board state when full search to terminal node is not possible.

# 12. Why is move ordering important?
#     Better move ordering leads to more pruning and faster evaluation.

# 13. What happens if Alpha-Beta is not applied?
#     Algorithm becomes plain Minimax and takes longer to compute.

# 14. Is Alpha-Beta always faster?
#     Yes, but speed varies — best when good move ordering exists.

# 15. Is Alpha-Beta used only for AI?
#     Yes, for adversarial game decision-making in search trees.
