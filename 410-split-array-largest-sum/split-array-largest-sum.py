class Solution:
    def splitArray(self, nums, k):
        def feasible(max_sum):
            parts = 1
            curr = 0
            for x in nums:
                if curr + x <= max_sum:
                    curr += x
                else:
                    parts += 1
                    curr = x
                    if parts > k:
                        return False
            return True

        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
