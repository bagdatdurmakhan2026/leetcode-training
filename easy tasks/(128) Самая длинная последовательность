class Solution(object):

  def longestConsecutive(self, nums):
    if not nums:
      return 0

    nums.sort()
    n = len(nums)

    mx = 1  # Минимальная длина для непустого массива равна 1
    cnt = 1  # Текущая длина последовательности

    l = 0
    r = 1

    while r < n:
      # 1. Если элементы одинаковые (дубликат), просто сдвигаем правый указатель
      if nums[r] == nums[r - 1]:
        r += 1
        continue

      # 2. Если следующий элемент на 1 больше предыдущего
      if nums[r] == nums[r - 1] + 1:
        cnt += 1
      else:
        # 3. Последовательность прервалась
        mx = max(mx, cnt)
        cnt = 1

      r += 1

    return max(mx, cnt)
                 
nums = [100,4,200,1,3,2]

print (Solution().longestConsecutive(nums))