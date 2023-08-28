# Given a 2D matrix, print all elements of the given matrix in diagonal order. For example, consider the following 5 X 4 input matrix.

# Example:

# 1     2     3     4   [00] [10 01] [20 11 02] [30 21 12 04]
# 5     6     7     8
# 9    10    11    12
# 13    14    15    16
# 17    18    19    20
# Diagonal printing of the above matrix is

# 1
# 5 2
# 9 6 3
# 13 10 7 4
# 17 14 11 8
# 18 15 12
# 19 16
# 20
row = 5
col = 4
M = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16],
     [17, 18, 19, 20]]

for i in range(0, row):
  for j in range(0, col):
    print(M[i][j], end='\t')
  print()

for i in range(0, row + col - 1):
  strt_col = max(0, i - row)
  c = min(i, col - strt_col, row)
  for j in range(0, c):
    print(M[min(row, i) - j - 1][strt_col + j], end="\t")
  print()