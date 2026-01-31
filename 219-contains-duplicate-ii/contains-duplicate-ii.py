class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_lookup = {}
        for i,num in enumerate(nums):
            if num in seen_lookup and abs(i - seen_lookup[num]) <= k:
                return True 
            seen_lookup[num] = i
        return False