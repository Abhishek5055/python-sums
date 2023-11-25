# Define a function to check if a square is a magic square
def is_magic_square(square):
    # Get the size (number of rows) of the square
    n = len(square)
    
    # Calculate the expected sum for a magic square
    expected_sum = n * (n**2 + 1) // 2
    
    # Check each row in the square
    for row in square:
        # Calculate the sum of elements in the current row
        row_sum = sum(row)
        
        # If the row sum is not equal to the expected sum, return False
        if row_sum != expected_sum:
            return False
    
    # Check each column in the square
    for j in range(n):
        # Calculate the sum of elements in the current column
        col_sum = sum(square[i][j] for i in range(n))
        
        # If the column sum is not equal to the expected sum, return False
        if col_sum != expected_sum:
            return False
    
    # Check the main diagonal (top-left to bottom-right)
    diagonal_sum = sum(square[i][i] for i in range(n))
    
    # If the diagonal sum is not equal to the expected sum, return False
    if diagonal_sum != expected_sum:
        return False
    
    # Check the secondary diagonal (top-right to bottom-left)
    diagonal_sum = sum(square[i][n - 1 - i] for i in range(n))
    
    # If the secondary diagonal sum is not equal to the expected sum, return False
    if diagonal_sum != expected_sum:
        return False
    
    # If all checks pass, return True, indicating it's a magic square
    return True

# Example usage:
# Define a square as a list of lists (a 3x3 matrix)
square = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

# Check if the square is a magic square using the defined function
if is_magic_square(square):
    print("It's a magic square!")
else:
    print("It's not a magic square.")
