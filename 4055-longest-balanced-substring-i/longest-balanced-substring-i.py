class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                
                # Check balance
                val = 0
                balanced = True
                for count in freq:
                    if count != 0:
                        if val == 0:
                            val = count
                        elif val != count:
                            balanced = False
                            break
                if balanced:
                    ans = max(ans, j - i + 1)
        return ans