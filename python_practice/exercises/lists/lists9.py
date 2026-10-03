# Exercise: Lists 9
# I AM NOT DONE
#
# A grid of numbers (a matrix) is stored as a list of rows - a list inside a list.
# Fix the ??? parts to get the right numbers out of the grid:
#   `center`       : the item in row 1, column 1  (should be 5)
#   `bottom_right` : the item in row 2, column 2  (should be 9)
# Then the code changes `matrix[0][2]` to 99.
# (Remember: rows and columns start counting at 0!)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

center       = matrix[???][???]
bottom_right = matrix[???][???]

matrix[0][2] = 99
