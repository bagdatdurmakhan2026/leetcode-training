def answer(nums):
    n = len(nums)
    if n <=1:
        return [0,0]
    start = 0
    mx = 1
    dir = 0
    best_l,best_r = 0,0
    for end in range(1,n):
        if nums[end] > nums[end-1]:
            curr_dir = 1
        elif nums[end] < nums[end-1]:
            curr_dir = -1
        else:
            curr_dir = 0
        if curr_dir==0:
            start = end
            dir = 0
        elif dir!=curr_dir:
            start = end - 1
            dir = curr_dir
        curr_max = end - start + 1
        if curr_max>mx:
            mx = curr_max
            best_l = start
            best_r = end
    return [best_l, best_r]
            
             
print(answer([2, 7, 5, 4, 4, 3]))  # Выведет [1, 3]
print(answer([1, 1]))              # Выведет [0, 0]