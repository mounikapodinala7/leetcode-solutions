class Solution:
    def isHappy(self, n: int) -> bool:
        def sqr(n):
            ans = 0
            while n > 0:
                rem = n % 10
                ans += rem * rem
                n //= 10
            return ans

        slow = n
        fast = n

        while True:
            slow = sqr(slow)
            fast = sqr(sqr(fast))
            if slow == fast:
                break

        return slow == 1