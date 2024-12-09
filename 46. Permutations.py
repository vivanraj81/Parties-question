# 46. Permutations

def fun(ind,s):
    if ind == len(nums):
        ans.append(s[:])
        return 
    for num in nums:
        if num not in s:
            fun(ind+1,s+[num])
ans =[]
fun(0,[])
return ans 