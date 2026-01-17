class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        hBars.sort()
        vBars.sort()

        max_h = curr = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                curr += 1
            else:
                curr = 1
            max_h = max(max_h, curr)

        max_v = curr = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                curr += 1
            else:
                curr = 1
            max_v = max(max_v, curr)

        side = min(max_h + 1, max_v + 1)
        return side * side
