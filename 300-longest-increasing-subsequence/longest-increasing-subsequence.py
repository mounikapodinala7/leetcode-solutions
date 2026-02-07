class Solution:
    def lengthOfLIS(self, a: List[int]) -> int:
        return len(reduce(lambda l,v:l[:(i:=bisect_left(l,v))]+[v]+l[i+1:],a,[]))