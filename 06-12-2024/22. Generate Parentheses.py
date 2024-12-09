22. Generate Parentheses

def genrate(s="",left=0,right=0):
    if len(s) == n*2:
        ans.append(s)
        return
        
    if left <n:
        genrate(s+'('left+1,right)
    if right<left:
        genrate(s+')'left,right+1)

    ans = []
    genrate()
    return result