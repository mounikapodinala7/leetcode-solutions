class Solution:
    def maxSumTwoNoOverlap(self, nums, L, M):
        n = len(nums)
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        def subarray_sum(i, length):
            return prefix[i + length] - prefix[i]
        
        ans = 0
        
        maxL = 0
        for i in range(L, n - M + 1):
            maxL = max(maxL, subarray_sum(i - L, L))
            ans = max(ans, maxL + subarray_sum(i, M))
        
        maxM = 0
        for i in range(M, n - L + 1):
            maxM = max(maxM, subarray_sum(i - M, M))
            ans = max(ans, maxM + subarray_sum(i, L))
        
        return ans