# Exercise: Lists 9
# I AM NOT DONE
#
# A list can hold other lists! A grid of numbers (called a MATRIX) is a list
# of rows, and each row is itself a list. Use two sets of square brackets: the
# first picks the row, the second picks the item in that row.
#
#     grid = [[1, 2], [3, 4]]
#     grid[1][0]     gives 3     (row 1, then item 0 in that row)
#
# Remember, rows and columns both start counting at 0!
# Fix the ??? so that:
#     `center`       is the item in row 1, column 1  (should be 5)
#     `bottom_right` is the item in row 2, column 2  (should be 9)
# The code then changes matrix[0][2] to 99.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

center       = matrix[???][???]
bottom_right = matrix[???][???]

matrix[0][2] = 99
