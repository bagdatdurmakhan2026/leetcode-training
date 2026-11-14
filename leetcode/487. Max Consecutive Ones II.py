def ans(nums):
    n = len(nums)
    l = None
    mx = 0
    start = 0
    for r in range(n):
        if nums[r] == 0:
            if l is not None:
             start =l + 1
            l = r
        mx = max(mx, r - start + 1)
    return mx        
        