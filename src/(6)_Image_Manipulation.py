# (6)_Image_Manipulation

from graphics import *

grid = [['X','O','O'],
        ['X','O','X'],
        ['X','X','O']]

data = [[1,2,3,4], [5,6,7,8]]



# adjency matrix: Represents existence of binary
#                 relationship.
#                 '1' if exists
#                 '0' if not
adj_matrix = [[0,1,1], 
              [1,0,0], 
              [1,0,0]]

# for row in range(3):
#     for column in range(3):
#         print(grid[row][column])

for row in range(len(data)):
    for column in range(len(data[0])):
        print(data[row][column])