class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        xor = 0

        for i in range(n + 1):
            xor ^= i

        for num in nums:
            xor ^= num

        return xor
