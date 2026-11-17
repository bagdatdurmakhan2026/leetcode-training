def ans(nums):
    n = len(nums)
    l = None
    cnt = 0
    for r in range(n):
        if nums[r] == 0:
            if l is None:
                l = r
            cnt += r - l + 1
        else:
            l = None
    return cnt
            
    
print(ans([1, 3, 0, 0, 2, 0, 0, 4]))