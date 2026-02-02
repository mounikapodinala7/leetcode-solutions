from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        target = k - 1

        sl = SortedList(nums[1 : dist + 2])

        current_sum = sum(sl[:target])
        min_sum = current_sum

        n = len(nums)
        for i in range(dist + 2, n):
            out_val = nums[i - (dist + 1)]
            in_val = nums[i]

            index_to_remove = sl.index(out_val)

            sl.remove(out_val)
            sl.add(in_val)

            index_of_add = sl.index(in_val)

            if index_to_remove < target:
                current_sum -= out_val

                if index_of_add < target:
                    current_sum += in_val
                else:
                    current_sum += sl[target - 1]
            else:
                if index_of_add < target:
                    current_sum += in_val
                    current_sum -= sl[target]

            min_sum = min(min_sum, current_sum)

        return nums[0] + min_sum
