class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        sub = [0] * m
        pos = defaultdict(list)
        for i in range(m): pos[t[i]].append(i)

        for i in s:
            for j in reversed(pos[i]):
                if j == 0:
                    sub[j] += 1
                else:
                    sub[j] += sub[j - 1]
        return sub[-1]