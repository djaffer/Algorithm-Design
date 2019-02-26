'''
A very hungry rabbit is placed in the center of of a garden,
represented by a rectangular N x M 2D matrix.
The values of the matrix will represent numbers of carrots
available to the rabbit in each square of the garden. If the garden
does not have an exact center, the rabbit should start in the
square closest to the center with the highest carrot count.
On a given turn, the rabbit will eat the carrots available on the
square that it is on, and then move up, down, left, or right,
choosing the the square that has the most carrots. If there are no
carrots left on any of the adjacent squares, the rabbit will go to
sleep. You may assume that the rabbit will never have to choose
between two squares with the same number of carrots.
Write a function which takes a garden matrix and returns the number
of carrots the rabbit eats. You may assume the matrix is rectangular with at least 1 row and 1 column, and that it is populated with non-negative integers. For example: 
[[5, 7, 8, 6, 3],
[0, 0, 7, 0, 4],
[4, 6, 3, 4, 9],
[3, 1, 0, 5, 8]]
Should return: 
27
'''

def get_center(garden):
  center_row = []
  center_col = []

  if len(garden) % 2 == 0:
      center_row = [(len(garden) //2) -1,len(garden) //2]
  else:
      center_row = [len(garden) //2]
  
  if len(garden[0]) %2 == 0:
      center_col = [(len(garden[0])//2) -1,len(garden[0])//2]
  else:
      center_col = [len(garden[0])//2]
  carrots = -1
  rowcol = [-1,-1]

  for i in range(len(center_row)):
    for j in range(len(center_col)):

      if garden[i][j] > carrots:
        carrots = garden[center_row[i]][center_col[j]]
        rowcol[0] = center_row[i]
        rowcol[1] = center_col[j]
  return rowcol

def search_carrots(garden, row, col):
    maxcarrots = 0
    nr = -1
    nc = -1
    
    for r in [-1,0,1]:
      for c in [-1,0,1]:
        if row + r >= 0 and row + r < len(garden) and \
                col + c >= 0 and col + c < len(garden[row]):
            if garden[row + r][col + c] > maxcarrots:
                maxcarrots = garden[row + r][col + c]
                nr = row + r
                nc = col + c

    numofcarrots = garden[row][col]
    garden[row][col] = 0

    if  nr != -1 and nc != -1 and maxcarrots > 0:
        numofcarrots += search_carrots(garden, nr, nc)

    return numofcarrots

def find_carrots(garden):
    if len(garden) == 0 or len(garden[0]) == 0:
        return 0

    
    rowcol = get_center(garden)
    if rowcol[0] == -1 is None or rowcol[1] == -1:
        return 0

    return search_carrots(garden,rowcol[0],rowcol[1])
    
if __name__ == "__main__":
    garden_case = [
        [5, 7, 8, 6, 3],
        [0, 0, 7, 0, 4],
        [4, 6, 3, 4, 9],
        [3, 1, 0, 5, 8]
    ]

    print(find_carrots(garden_case))
    
    