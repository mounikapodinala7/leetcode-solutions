class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def dfs(s, l, r):
            if len(s) == 2 * n:
                res.append(s)
                return
            if l < n:
                dfs(s + "(", l + 1, r)
            if r < l:
                dfs(s + ")", l, r + 1)

        dfs("", 0, 0)
        return res
