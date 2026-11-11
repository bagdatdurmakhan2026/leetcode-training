class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0          
        cnt = 0
        for i in range(2, n):
            is_prime = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                cnt += 1
        return cnt
        """
        :type n: int
        :rtype: int
        """
        