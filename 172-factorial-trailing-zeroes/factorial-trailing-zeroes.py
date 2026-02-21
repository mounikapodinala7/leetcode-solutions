class Solution:
    def trailingZeroes(self, n: int) -> int:

        if n < 5: return 0
        fives, ans = 5, 0
        k = int(log(n, 5))
        
        for _ in range(k):
            cnt = n // fives
            ans+= cnt
            fives*= 5
        return ans
    