n=4
def isValid(n, maze, x, y, s):
    if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1 and s[x][y] == 0:
        return True
    return False
def RatMaze(n,maze,move_x,move_y,x,y,s):
  if x==n-1 and y==n-1:
    return True
  for i in range(n):
    x_new=x+move_x[i]
    y_new=y+move_y[i]
    if isValid(n,maze,x_new,y_new,s):
      s[x_new][y_new]=1
      if RatMaze(n,maze,move_x,move_y,x_new,y_new,s):
        return True
      s[x_new][y_new]=0
  return False


maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]
s=[[0 for i in range(n)] for i in range(n)]
s[0][0]=1
move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]
if RatMaze(n,maze,move_x,move_y,0,0,s):
  for i in range(n):
    for j in range(n):
      print(s[i][j],end=" ")
    print()
else:
  print("No solution")