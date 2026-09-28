def asd(s):
    ch = set()
    ml = 0
    lf = 0
    for r in range(len(s)):
        while s[r] in ch:
            ch.remove(s[lf])
            lf+=1
        ch.add(s[r])
        ml = max(ml,r-lf+1)
    return ml
ss = str(input())
ass= asd(ss)
print(ass)
