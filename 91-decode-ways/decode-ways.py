class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1} #also helpful if len is just 1.

        for i in range(len(s)-1, -1, -1):

            if s[i] == "0":
                dp[i] = 0
            else:
                #dp[i] = dp[i+1] + dp[i+2] if it can make 2 digits, else just dp[i+1]
                dp[i] = dp[i+1]

            if i+1 < len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1]in"0123456")):
                dp[i] += dp[i+2]

        return dp[0]
        