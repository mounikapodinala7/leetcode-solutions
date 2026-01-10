class Solution:
    def smallestDivisor(self, nums, threshold):
        def feasible(d):
            total = 0
            for x in nums:
                total += (x + d - 1) // d
                if total > threshold:
                    return False
            return True
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
