def answer(nums):
    n = len(nums)
    if n <= 1:
        return [0, 0]
    best_l, best_r = 0, 0
    max_len = 1
    l = 0
    direction = 0  # 1: возрастает, -1: убывает, 0: не определено
    for r in range(1, n):
        if nums[r] > nums[r - 1]:
            current_dir = 1
        elif nums[r] < nums[r - 1]:
            current_dir = -1
        else:
            current_dir = 0
        if current_dir == 0 or (direction != 0 and current_dir != direction):
            if r - l > max_len:
                max_len = r - l
                best_l, best_r = l, r - 1
            if current_dir != 0:
                l = r - 1
                direction = current_dir
            else:
                l = r
                direction = 0
        else:
            if direction == 0:
                l = r - 1
                direction = current_dir
    if n - l > max_len:
        max_len = n - l
        best_l, best_r = l, n - 1     
    return [best_l, best_r]
print(answer([2, 7, 5, 4, 4, 3]))  # Выведет [1, 3]
print(answer([1, 1]))              # Выведет [0, 0]