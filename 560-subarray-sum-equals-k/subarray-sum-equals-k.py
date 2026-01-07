from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        prefix_count = defaultdict(int)
        prefix_count[0] = 1   # important!

        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            if (curr_sum - k) in prefix_count:
                count += prefix_count[curr_sum - k]

            prefix_count[curr_sum] += 1

        return count
