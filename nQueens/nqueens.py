def nqueens(n):
    # implementing depth-limited with backtracking
    def dfs(board, row, cols, diag1, diag2):
        if row == n: # if we reach all the levels, then we have a solution
            return board
        for col in range(n):
            if col not in cols and row + col not in diag1 and row - col not in diag2: # check for validity
                board[row] = col # if checks passed, place queen at given column
                cols.add(col) # make sure no queen will be in the same column
                diag1.add(row + col) # adds positive diagonals
                diag2.add(row - col) # adds negative diagonals
                result = dfs(board, row + 1, cols, diag1, diag2) # perform same search on the next row
                if result: # if we get to n, return true, else the conditions were broken somewhere
                    return result
                board[row] = -1 # if not, come back one step and try again
                cols.remove(col) # remove invalid column
                diag1.remove(row + col) # remove invalid positive diagonal
                diag2.remove(row - col) # remove negative diagonal
        return False

    board = [-1] * n
    return dfs(board, 0, set(), set(), set())

nqueens(4)

### Thought Process Below ###

    # TODO 1: set all the queens to row 0 on the board
    #   0 # # #
    #   0 # # #
    #   0 # # #
    #   0 # # #
    # Represented by [0,0,0,0]

    # TODO 2: Initiate a sets for taken rows and diagonals

    # TODO 3:
    # If we get to n, then return the solution

    # TODO 4: Recursion
    # [ 0 , 0 , 0, 0 ]
    # i,j = 0,i+1

    #check validities and add elements to solution board accordingly
    #add elements to set every turn

    # TODO 5: Backtracking
    # implement following algorithm:
        # if we have no solution from descending down a logic tree ex: [0,2,1,0]:
            # go back one step and change the previous value
            # do this until solution found