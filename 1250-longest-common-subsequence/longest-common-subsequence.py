class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1

        prev = [0] * (len(text2) + 1)

        for c1 in text1:
            curr = [0]
            for j, c2 in enumerate(text2):
                if c1 == c2:
                    curr.append(prev[j] + 1)
                else:
                    curr.append(max(curr[-1], prev[j + 1]))
            prev = curr

        return prev[-1]
