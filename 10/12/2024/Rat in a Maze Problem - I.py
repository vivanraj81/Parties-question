# Rat in a Maze Problem - I


rows, cols = len(mat), len(mat[0])
visited = [[0 for _ in range(cols)] for _ in range(rows)]
ans = []
def solve(i,j, path):
    if i == rows-1 and j == cols-1:
        ans.append(path)
    
    if  i+1 < rows and not visited[i+1][j] and mat[i+1][j] == 1:    
        visited[i][j] = 1
        solve(i+1, j, path +'D') 
        visited[i][j] = 0
        
    if  j-1 >= 0 and not visited[i][j-1] and mat[i][j-1] == 1:   
        visited[i][j] = 1
        solve(i, j-1, path +'L') 
        visited[i][j] = 0
    if  j+1 < cols and not visited[i][j+1] and mat[i][j+1] == 1: 
        visited[i][j] = 1
        solve(i, j+1, path +'R') 
        visited[i][j] = 0
    if  i-1 >= 0 and not visited[i-1][j] and mat[i-1][j] == 1:
        visited[i][j] = 1
        solve(i-1, j, path +'U')  
        visited[i][j] = 0
        
solve(0,0, "")
return ans