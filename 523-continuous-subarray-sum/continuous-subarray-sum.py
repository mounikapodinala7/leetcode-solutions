class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index = {0: -1}
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            rem = curr_sum % k
            if rem in remainder_index:
                if i - remainder_index[rem] >= 2:
                    return True
            else:
                remainder_index[rem] = i
        return False
