class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = {0: 1}
        curr_sum = 0
        ans = 0
        for num in nums:
            curr_sum += num
            rem = curr_sum % k
            ans += remainder_count.get(rem, 0)
            remainder_count[rem] = remainder_count.get(rem, 0) + 1
        return ans
