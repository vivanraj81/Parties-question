# 39. Combination Sum

def backtrack(start, ans, sample, target, sum):
    if sum == target:
        ans.append(list(sample))
        return
    if sum > target:
        return
    for end in range(start, len(candidates)):
        if end > start and candidates[end] == candidates[end - 1]:
            continue
        sample.append(candidates[end])
        sum += candidates[end]
        backtrack(end, ans, sample, target, sum)  
        sum -= candidates[end]
        sample.pop()
candidates.sort()  
ans = []
sample = []
backtrack(0, ans, sample, target, 0)
return ans
