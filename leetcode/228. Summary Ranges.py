def ans(nums):
    n = len(nums)
    res = []
    l = None
    for r in range(n):
        if l is None:
            l=r
        if r == n - 1 or nums[r + 1] != nums[r] + 1:
            if l == r:
                res.append(str(nums[l]))
            else:
                res.append(f"{nums[l]}->{nums[r]}")
            l = None
    return res
print(ans([0, 1, 2, 4, 5, 7]))