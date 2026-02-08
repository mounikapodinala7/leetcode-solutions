class Solution:
    def cloneGraph(self, n: Optional['Node']) -> Optional['Node']:
        return n and (f:=lambda n,d={}:d.get(v:=n.val,0) or (setitem(d,v,Node(v)),setattr(d[v],'neighbors',[*map(f,n.neighbors)])) and d[v])(n)