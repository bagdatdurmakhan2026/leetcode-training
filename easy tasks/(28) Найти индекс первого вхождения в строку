class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        else:
            n = len(haystack)
            m = len(needle)
            for i in range(n-m+1):
                res = True
                for j in range(m):
                    if haystack[i+j]!=needle[j]:
                        res = False
                        break
                if res:
                    return i
        return -1
        
haystack = "leetcode"
needle = "sad"
print(Solution().strStr(haystack,needle))
# Для двух строк needle и haystack вернуть индекс первого вхождения needle в haystack или -1 если needle не является частью haystack. Для этого решение проста сначала проверить needle not in haystack  return -1 else:
# \