# -------------------
# (9)_Game_of_Life
#--------------------


from graphics import *
import random



def create_row(n):
    row = []
    for num in range(n):
        row.append(' ')
    return row

def create_grid(n,m):
    grid = []
    for row in range(n):
        grid.append(create_row(m))
    return grid

# print(create_grid(2,3))

def flip():
    
    if random.random() <= 0.5:
        print('head')

    else:
        print('tails')


# def roll():
#     randomNum = random.random()

#     if randomNum <= (1*0.1666):
#         print('1')
#     elif randomNum <= (2*0.1666):
#         print('2')
#     elif randomNum <= (3*0.1666):
#         print('3')
#     elif randomNum <= (4*0.1666):
#         print('4')
#     elif randomNum <= (5*0.1666):
#         print('5')
#     else:
#         print('6')

def populate(grid, prob):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if random.random() <= prob:
                grid[i][j] = '*'

    return grid


def neighbours(grid, row, column):
    liveNeighbors = 0
    rows = len(grid)
    columns = len(grid[0])
    for i in range(max(0, row-1), min(row+2, rows)):
        for j in range(max(0, column-1), min(column+2, columns)):
            if i == row and j == column:  # Skip the center cell itself
                continue
            elif grid[i][j] == '*':
                liveNeighbors += 1
    return liveNeighbors



def visualize(grid):
    rows = len(grid) 
    columns = len(grid[0]) 

    separator = ''
    for i in range(columns*4 + 1):
        separator += '-'
    print(separator)

    for i in range(rows):
        line = '| '
        for j in range(columns):
            line += grid[i][j] + ' | '
        print(line)
        print(separator)


def evolve(grid):
    alive = '*'
    dead = ' '
    rows = len(grid)
    cols = len(grid[0])
    newGrid = create_grid(rows,cols)

    for i in range(rows):
        for j in range(cols):
            numNeigh = neighbours(grid,i,j)
            cell = grid[i][j]
            

            if cell == dead and numNeigh == 3:
                newGrid[i][j] = alive
                    
            elif cell == alive: # cell is alive
                if numNeigh < 2 or numNeigh > 3:
                    newGrid[i][j] = dead  # Cell dies
                else:
                    newGrid[i][j] = alive  # Cell stays alive
            else:
                continue


    return newGrid


# grid1 = create_grid(5,5)

# populate(grid1,0.5)




def create_grid_visual(rows, cols, window):
    grid_visual = create_grid(rows,cols)

    p_w = window.getWidth() // cols # cols
    p_h = window.getHeight() // rows # rows
    
    for i in range(rows):
        for j in range(cols):
            grid_visual[i][j] = Rectangle(Point(j*p_w, i*p_h),
                                          Point( (j + 1)*p_w, (i+1)*p_h))
            grid_visual[i][j].setFill(color_rgb(0,0,0))
            grid_visual[i][j].setOutline(color_rgb(50,50,50))
            grid_visual[i][j].draw(window)

    return grid_visual

def mirror(grid, grid_visual):
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '*':
                grid_visual[i][j].setFill(color_rgb(0,255,0))

            else:
                grid_visual[i][j].setFill(color_rgb(0,0,0))


def place_glider(x, y, grid):
    """Places a glider with top-left cell at (x, y)."""
    glider_pattern = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for dx, dy in glider_pattern:
        grid[x + dx][y + dy] = '*'


def place_eater(x,y, grid):
    eater_pattern = [(0,0), (0,1), (1,0),(2,1),(2,2),(2,3),(3,3)]
    for dx, dy in eater_pattern:
        grid[x+dx][y+dy]='*'

def place_glider_gun(x, y, grid):
    """Place a Gosper Glider Gun with the top-left cell at (x, y)."""
    gun_pattern = [
        (5, 1), (5, 2), (6, 1), (6, 2),
        (5, 11), (6, 11), (7, 11), (4, 12), (8, 12), (3, 13), (9, 13), (3, 14), (9, 14),
        (6, 15), (4, 16), (8, 16), (5, 17), (6, 17), (7, 17), (6, 18),
        (3, 21), (4, 21), (5, 21), (3, 22), (4, 22), (5, 22), (2, 23), (6, 23),
        (1, 25), (2, 25), (6, 25), (7, 25),
        (3, 35), (4, 35), (3, 36), (4, 36)
    ]
    for dx, dy in gun_pattern:
        grid[x + dx][y + dy] = '*'


window = GraphWin('Game of Life', 500, 500, autoflush=False)
ca_grid = create_grid(50,50)
grid_visual = create_grid_visual(50, 50, window)
#populate(ca_grid,0.5)
#place_glider(5, 5, ca_grid)  # Initialize the glider at position (10, 10)
place_glider_gun(5,5,ca_grid)
place_eater(40,40,ca_grid)




try:
    while True:
        mirror(ca_grid, grid_visual)
        window.update()
        ca_grid = evolve(ca_grid)
except GraphicsError:
    print("Window closed")

