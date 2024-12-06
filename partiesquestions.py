# 526. Beautiful Arrangement

# def backtrack(index):
#     nonlocal count
#     if index == n + 1:
#         count += 1
#         return
#     for i in range(1, n + 1):
#         if not visited[i] and (i % index == 0 or index % i == 0):
#             visited[i] = True
#             backtrack(index + 1)
#             visited[i] = False
# count = 0
# visited = [False] * (n + 1)
# backtrack(1)
# return count

# /-------------------------------------------------------------------------------------------------------------------------------------/

# 22. Generate Parentheses

# def genrate(s="",left=0,right=0):
#     if len(s) == n*2:
#         ans.append(s)
#         return
        
#     if left <n:
#         genrate(s+'('left+1,right)
#     if right<left:
#         genrate(s+')'left,right+1)

#     ans = []
#     genrate()
#     return result

# /-------------------------------------------------------------------------------------------------------------------------------------/

# 17. Letter Combinations of a Phone Number

# if not digits:
#     return []
# letters = {
#     '2': 'abc',
#     '3': 'def',
#     '4': 'ghi',
#     '5': 'jkl',
#     '6': 'mno',
#     '7': 'pqrs',
#     '8': 'tuv',
#     '9': 'wxyz',
# }
    
# def fun(ind,s):
#     if ind == len(digits):
#         ans.append(s)
#         return 
#     for i in letters[digits[ind]]:
#         fun(ind+1,s+i)

# ans=[]
# fun(0,"")
# return ans

# /-------------------------------------------------------------------------------------------------------------------------------------/

# 46. Permutations

# def fun(ind,s):
#     if ind == len(nums):
#         ans.append(s[:])
#         return 
#     for num in nums:
#         if num not in s:
#             fun(ind+1,s+[num])
# ans =[]
# fun(0,[])
# return ans 

 
# /-------------------------------------------------------------------------------------------------------------------------------------/

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


# /-------------------------------------------------------------------------------------------------------------------------------------/