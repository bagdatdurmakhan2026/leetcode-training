def answer(nums):
    n = len(nums)
    left = None
    mx = 0
    for r in range(n):
        if nums[r] == 1:
            if left is None:
                mx = max(mx,r)
        else:
            mx = max(mx, (r-left)//2)
        left = r
    mx = max(mx,((n-1)-left))
    return mx 
nums = [1, 0, 0, 0, 1, 0, 1]
print(answer(nums))