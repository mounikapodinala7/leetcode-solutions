class Solution:
    def minimumDeletions(self, s: str) -> int:
        return min(accumulate((1-2*(c=='a') for c in s),initial=s.count('a')))