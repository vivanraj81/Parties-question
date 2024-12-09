# 17. Letter Combinations of a Phone Number

if not digits:
    return []
letters = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}
    
def fun(ind,s):
    if ind == len(digits):
        ans.append(s)
        return 
    for i in letters[digits[ind]]:
        fun(ind+1,s+i)

ans=[]
fun(0,"")
return ans