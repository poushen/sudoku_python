import numpy as np
count = 0

#grid = [[9, 0, 6, 0, 7, 0, 4, 0, 3],
#       [0, 0, 0, 4, 0, 0, 2, 0, 0],
#       [0, 7, 0, 0, 2, 3, 0, 1, 0],
#       [5, 0, 0, 0, 0, 0, 1, 0, 0],
#       [0, 4, 0, 2, 0, 8, 0, 6, 0],
#       [0, 0, 3, 0, 0, 0, 0, 0, 5],
#       [0, 3, 0, 7, 0, 0, 0, 5, 0],
#       [0, 0, 7, 0, 0, 5, 0, 0, 0],
#       [4, 0, 5, 0, 1, 0, 7, 0, 8]]

#grid = [[ 0, 8, 0, 0, 9, 3, 0, 7, 0 ],
#        [6, 9, 0, 4, 7, 0, 0, 0, 2 ],
#        [0, 0, 1, 0, 0, 2, 6, 0, 0 ],
#        [0, 2, 0, 9, 3, 0, 0, 1, 0 ],
#        [9, 0, 0, 7, 0, 4, 0, 0, 5 ],
#        [7, 1, 0, 0, 2, 0, 0, 3, 0 ],
#        [0, 0, 8, 3, 0, 0, 1, 0, 7 ],
#        [3, 0, 9, 0, 0, 7, 0, 0, 8 ],
#        [0, 4, 0, 2, 5, 0, 0, 6, 9 ]]

grid = [[0, 0, 0, 8, 0, 0, 0, 0, 9 ],
        [0, 1, 9, 0, 0, 5, 8, 3, 0 ],
        [0, 4, 3, 0, 1, 0, 0, 0, 7 ],
        [4, 0, 0, 1, 5, 0, 0, 0, 3 ],
        [0, 0, 2, 7, 0, 4, 0, 1, 0 ],
        [0, 8, 0, 0, 9, 0, 6, 0, 0 ],
        [0, 7, 0, 0, 0, 6, 3, 0, 0 ],
        [0, 3, 0, 0, 7, 0, 0, 8, 0 ],
        [9, 0, 4, 5, 0, 0, 0, 0, 1 ]]

def possible(y,x,n):
    global grid
    # n is the number we want to fill in
    
    # check if n already existed in vertical (y) axis
    # if exists, return False (not possible)
    for i in range(9):
        if grid[y][i] == n:
            return False
    
    # check horizontal (x) axix
    for i in range(9):
        if grid[i][x] == n:
            return False
        
    #check the 3x3 sub grid
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    
    # return True if pass all 3 checks
    return True

def solve():
    global grid, count
    for y in range(9):
        for x in range(9):
            # find blank positions in the grid (value = 0)
            if grid[y][x] == 0:
                # loop n from 1-9
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        
                        # This is where backtracking happens
                        # Reset the latest position back to 0 and try with new n value
                        grid[y][x] = 0
                return
    count = count + 1
    print("id:{}".format(count))
    print(np.matrix(grid))
    # input('More?')
    
solve()
