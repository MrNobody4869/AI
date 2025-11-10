# Implementing Backtracking and Branch & Bound for N-Queens Problem
# N-Queens: Place N queens on an N×N board such that no two queens attack each other.

# Function to print the chessboard
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            # 1 indicates queen, 0 is empty
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()
    print()

# --------------------------------------------------
# BACKTRACKING APPROACH
# --------------------------------------------------
# Backtracking tries placing queens row by row.
# If a position leads to conflict later, we undo and try another position.

def is_safe_backtracking(board, row, col, n):
    # Check the same column above current row
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True  # Position is safe

def solve_backtracking(board, row, n):
    # If all queens are placed successfully, return true
    if row >= n:
        return True

    # Try placing queen in each column of current row
    for col in range(n):
        if is_safe_backtracking(board, row, col, n):
            board[row][col] = 1

            # Recursive call for next row
            if solve_backtracking(board, row + 1, n):
                return True

            # Backtrack if placement fails later
            board[row][col] = 0

    return False

def n_queens_backtracking(n):
    # Board initialization
    board = [[0] * n for _ in range(n)]
    
    # Start solving
    if solve_backtracking(board, 0, n):
        print("\nSolution using Backtracking:")
        print_board(board, n)
    else:
        print("No solution exists!")

# --------------------------------------------------
# BRANCH AND BOUND APPROACH
# --------------------------------------------------
# Branch and Bound uses extra arrays to track attacked columns and diagonals.
# It avoids exploring invalid branches early, making it faster than backtracking.

def solve_branch_and_bound(board, row, cols, left_diagonals, right_diagonals, n):
    # If all rows are done, solution found
    if row >= n:
        return True

    for col in range(n):
        # Check if column and diagonals are free
        if not cols[col] and not left_diagonals[row - col + n - 1] and not right_diagonals[row + col]:

            # Place queen and mark attack paths
            board[row][col] = 1
            cols[col] = left_diagonals[row - col + n - 1] = right_diagonals[row + col] = True

            # Move to next row
            if solve_branch_and_bound(board, row + 1, cols, left_diagonals, right_diagonals, n):
                return True

            # Backtrack: remove queen and unblock paths
            board[row][col] = 0
            cols[col] = left_diagonals[row - col + n - 1] = right_diagonals[row + col] = False

    return False

def n_queens_branch_and_bound(n):
    # Board and helper arrays initialization
    board = [[0] * n for _ in range(n)]
    cols = [False] * n
    left_diagonals = [False] * (2 * n - 1)
    right_diagonals = [False] * (2 * n - 1)

    # Start solving
    if solve_branch_and_bound(board, 0, cols, left_diagonals, right_diagonals, n):
        print("\nSolution using Branch and Bound:")
        print_board(board, n)
    else:
        print("No solution exists!")

# --------------------------------------------------
# MENU-DRIVEN PROGRAM
# --------------------------------------------------
# User can choose method. Good for comparing both approaches.

def main():
    while True:
        print("\n=== N-Queens Problem ===")
        print("1. Solve using Backtracking")
        print("2. Solve using Branch and Bound")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter the value of N: "))
            n_queens_backtracking(n)

        elif choice == "2":
            n = int(input("Enter the value of N: "))
            n_queens_branch_and_bound(n)

        elif choice == "3":
            print("Exiting Program...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()














































# Viva: What is a Constraint Satisfaction Problem (CSP)?
# CSP is a problem where we must assign values to variables under given constraints.
# Example: N-Queens, Sudoku, Graph Coloring.

# Viva: Why is N-Queens a CSP?
# In N-Queens, each queen is a variable, possible positions are values, and constraints prevent queens attacking each other.

# Viva: What technique is used here?
# We are solving CSP using Backtracking and Branch & Bound approaches.

# Viva: What is Backtracking?
# Backtracking is a depth-first search technique.
# We place queens one by one; if constraints break, we undo the step and try another option.

# Viva: Why backtracking works for N-Queens?
# It explores possible board configurations systematically and backtracks when conflicts occur.

# Viva: Limitation of backtracking?
# Slow for large N because it explores many invalid possibilities.

# Viva: What is Branch and Bound?
# Branch and Bound prunes the search tree by eliminating impossible partial solutions early.
# It avoids searching branches where constraints are already violated.

# Viva: Difference between Backtracking and Branch & Bound?
# Backtracking checks validity after placement.
# Branch & Bound keeps track of restricted rows, columns, and diagonals to prune early.
# Branch & Bound is faster because it blocks invalid paths before exploring them.

# Viva: What constraints are used in N-Queens?
# No two queens in same row, column, left diagonal, or right diagonal.

# Viva: Time complexity?
# Worst-case exponential: O(N!) for naive backtracking; Branch & Bound is faster but still exponential.

# Viva: Space complexity?
# O(N^2) for board representation, plus O(N) auxiliary arrays in Branch & Bound.

# Viva: What is solution output?
# A board placing N queens where none attack each other.

# Viva: Why CSPs use these techniques?
# They efficiently explore solution space and prune invalid states to reach solutions faster.

# Viva: Practical applications of CSP?
# Scheduling, resource allocation, timetabling, map coloring, puzzle solving, AI planning.

# Viva: Why diagonals matter in N-Queens?
# Queens attack horizontally, vertically, and diagonally, so diagonal checks ensure constraint satisfaction.

# Viva: Example of another CSP?
# Graph coloring: assign colors to nodes such that adjacent nodes have different colors.
