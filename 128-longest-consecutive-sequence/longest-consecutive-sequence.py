class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        def find_ans(num):
            if num in unique_ele:
                if num not in dp:
                    dp[num] = find_ans(num-1) + 1
                return dp[num]
            else:
                return 0
                        
        dp = {}
        unique_ele = set()
        ans = 0
        for num in nums:
            unique_ele.add(num)
        
        for num in nums:
            ans = max(ans, find_ans(num))
        return ans