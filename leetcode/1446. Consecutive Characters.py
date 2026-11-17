def ans(ss):
    n = len(ss)
    l = None
    mx = 0
    for r in range(n):
        if l is None or ss[r] != ss[l]:
            l = r
        mx = max(mx, r - l + 1)
    return mx
print(ans('abbcccddddeeeeedcba'))