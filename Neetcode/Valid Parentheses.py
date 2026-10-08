class Solution:
    def isValid(self, s: str) -> bool:
        bib = { 
            ')': '(', '}': '{', ']': '['
        }
        arr = []
        for i in s:
            if i in bib:
                if not arr or arr.pop()!= bib[i]:
                    return False
            else:
                arr.append(i)
        return len(arr) == 0