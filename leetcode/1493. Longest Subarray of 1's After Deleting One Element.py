def ans(nums):
    n = len(nums)
    l = None
    mx = 0
    start = 0
    for r in range(nums):
        if nums[r]==0:
            if l is None:
                start = l + 1
                
        l = r
        mx = max(mx, r - start)
    return mx        
        
    

