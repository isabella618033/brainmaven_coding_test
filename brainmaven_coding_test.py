
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# this test case was creted to illustrate an island with 2  "top left corner" as starting points
grid3 = [
  ["1","1","1","0","0"],
  ["1","0","1","0","0"],
  ["0","1","1","0","0"],
  ["0","1","1","1","1"]
]
def count_island(grid):
    m = len(grid)
    n = len(grid[0])

    print("=================================================")
    print("\nOrigional grid\n")
    for i in range(m):
        print(grid[i])

    # this loop is for finding out the top left corner of every island, and label it with integer
    island_count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                if ((i-1 < 0) or grid[i-1][j] == '0') and ( (j-1 < 0) or grid[i][j-1] == '0'):
                    island_count += 1
                    grid[i][j] = island_count

    # this loop is for scanning each cell, if it is connected some to other cell with label,
    # copy the label to the current cell
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                if (i-1 >= 0) and grid[i-1][j] != '0':
                    grid[i][j] = grid[i-1][j]

                    # this if block is for handling case in grid3,
                    # where and island have 2 "top left corner"
                    if (j-1 >= 0) and grid[i][j-1] != '0' and grid[i][j-1] != grid[i-1][j]:
                        grid[i][j-1] = grid[i-1][j]
                        island_count -= 1

                if (j-1 >= 0) and grid[i][j-1] != '0':
                    grid[i][j] = grid[i][j-1]

    print("\nUpdated grid with island label\n")
    for i in range(m):
        print(grid[i])

    print("\nNumber of island: ", island_count)

count_island(grid1)
count_island(grid2)
count_island(grid3)

# Expected result
# =================================================
#
# Origional grid
#
# ['1', '1', '1', '1', '0']
# ['1', '1', '0', '1', '0']
# ['1', '1', '0', '0', '0']
# ['0', '0', '0', '0', '0']
#
# Updated grid with island label
#
# [1, 1, 1, 1, '0']
# [1, 1, '0', 1, '0']
# [1, 1, '0', '0', '0']
# ['0', '0', '0', '0', '0']
#
# Number of island:  1
# =================================================
#
# Origional grid
#
# ['1', '1', '0', '0', '0']
# ['1', '1', '0', '0', '0']
# ['0', '0', '1', '0', '0']
# ['0', '0', '0', '1', '1']
#
# Updated grid with island label
#
# [1, 1, '0', '0', '0']
# [1, 1, '0', '0', '0']
# ['0', '0', 2, '0', '0']
# ['0', '0', '0', 3, 3]
#
# Number of island:  3
# =================================================
#
# Origional grid
#
# ['1', '1', '1', '0', '0']
# ['1', '0', '1', '0', '0']
# ['0', '1', '1', '0', '0']
# ['0', '1', '1', '1', '1']
#
# Updated grid with island label
#
# [1, 1, 1, '0', '0']
# [1, '0', 1, '0', '0']
# ['0', 1, 1, '0', '0']
# ['0', 1, 1, 1, 1]
#
# Number of island:  1
