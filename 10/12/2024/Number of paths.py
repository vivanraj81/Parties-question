# Number of paths    
    
def numberOfPaths(self, m, n):
    def backtrack(x, y):
        if x == m - 1 and y == n - 1:
            return 1
        if x >= m or y >= n:
            return 0
        return backtrack(x + 1, y) + backtrack(x, y + 1)

    return backtrack(0, 0)

