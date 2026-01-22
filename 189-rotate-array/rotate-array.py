class Solution:
    def rever(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    def rotate(self, nums: list[int], k: int) -> None:
        length = len(nums)
        k %= length
        if k == 0:
            return
        someMid = length - k
        self.rever(nums, 0, someMid - 1)
        self.rever(nums, someMid, length - 1)
        self.rever(nums, 0, length - 1)