526. Beautiful Arrangement

def backtrack(index):
    nonlocal count
    if index == n + 1:
        count += 1
        return
    for i in range(1, n + 1):
        if not visited[i] and (i % index == 0 or index % i == 0):
            visited[i] = True
            backtrack(index + 1)
            visited[i] = False
count = 0
visited = [False] * (n + 1)
backtrack(1)
return count
