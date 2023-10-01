Assignment 3 

function solve_n_queens(N):
    Initialize an empty chessboard of size N×N
    Initialize an empty list to store solutions

    function is_safe(row, col):
        Check if it's safe to place a queen in the (row, col) cell
        - Check the row for any other queens
        - Check the upper-left diagonal for any other queens
        - Check the lower-left diagonal for any other queens
        Return True if safe, False otherwise

    function backtrack(col):
        If col is equal to N, add the current configuration to the list of solutions
        For each row in range(N):
            If is_safe(row, col):
                Place a queen in the (row, col) cell
                Recursively call backtrack(col + 1)
                Remove the queen from the (row, col) cell (backtrack)

    Start the backtracking process with col = 0
    Return the list of solutions

N = 4 (or any desired board size)
solutions = solve_n_queens(N)
Print all solutions