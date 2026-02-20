import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2 or k == 0:
            return []
        result = []
        visited = set()
        minHeap = []
        heapq.heappush(minHeap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))
        while minHeap and len(result) < k:
            sum_, i, j = heapq.heappop(minHeap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(minHeap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
        return result