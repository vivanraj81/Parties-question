# 1219. Path with Maximum Gold

m = len(grid)
n = len(grid[0])
max_gold = 0

def find(i, j):
    if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == 0:
        return 0
    cur = grid[i][j]
    grid[i][j] = 0  
    top = find(i - 1, j)
    bottom = find(i + 1, j)
    left = find(i, j - 1)
    right = find(i, j + 1)
    grid[i][j] = cur  
    return cur + max(top, bottom, left, right)

for i in range(m):
    for j in range(n):
        if grid[i][j] != 0:
            max_gold = max(max_gold, find(i, j))

return max_gold