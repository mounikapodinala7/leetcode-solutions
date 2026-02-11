import sys
# Increase recursion limit for deep Segment Trees
sys.setrecursionlimit(200000)
class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
            
        # 1. Fast check for all elements
        all_e = set()
        all_o = set()
        for x in nums:
            if x & 1: all_o.add(x)
            else: all_e.add(x)
            
        if len(all_e) == len(all_o):
            return n
        if not all_e or not all_o:
            return 0
            
        # 2. Precompute Next Occurrence
        # next_occ[i] index of next occurrence of nums[i]. If none -> n.
        next_occ = [n] * n
        last_seen = {}
        # Iterate backwards to fill next_occ
        for i in range(n - 1, -1, -1):
            val = nums[i]
            if val in last_seen:
                next_occ[i] = last_seen[val]
            last_seen[val] = i
            
        # 3. Initial Balance Calculation (Start at L=0)
        # balance[i] = UniqueEven(0..i) - UniqueOdd(0..i)
        initial_balance = [0] * n
        curr_e = set()
        curr_o = set()
        bal = 0
        for i, x in enumerate(nums):
            if x & 1:
                if x not in curr_o:
                    bal -= 1
                    curr_o.add(x)
            else:
                if x not in curr_e:
                    bal += 1
                    curr_e.add(x)
            initial_balance[i] = bal
            
        # 4. Build Segment Tree
        # Tree size: 4*n
        # tree_min[node], tree_max[node], lazy[node]
        self.n = n
        self.tree_min = [0] * (4 * n)
        self.tree_max = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        
        self._build(initial_balance, 1, 0, n - 1)
        
        max_len = 0
        
        # 5. Main Loop (Sliding L)
        for L in range(n):
            # Optimization: Early Exit
            if L + max_len >= n: break
            
            # Optimization: Query Bound
            # Find rightmost R >= L + max_len with balance 0
            query_start = L + max_len
            idx = self._find_last_zero(1, 0, n - 1, query_start)
            
            if idx != -1:
                length = idx - L + 1
                if length > max_len:
                    max_len = length
            
            # Prepare for next step (L -> L+1)
            # Remove nums[L]
            if L < n - 1:
                end = next_occ[L] - 1
                if end >= L + 1:
                    # Update range [L+1, end]
                    # If nums[L] Even: lost 1 even -> balance decreases by 1 (-1)
                    # If nums[L] Odd: lost 1 odd -> balance increases by 1 (+1)
                    delta = -1 if (nums[L] % 2 == 0) else 1
                    self._update(1, 0, n - 1, L + 1, end, delta)
        
        return max_len
    # --- SegTree Methods ---
    def _build(self, data, node, start, end):
        if start == end:
            self.tree_min[node] = data[start]
            self.tree_max[node] = data[start]
        else:
            mid = (start + end) // 2
            self._build(data, 2 * node, start, mid)
            self._build(data, 2 * node + 1, mid + 1, end)
            self.tree_min[node] = min(self.tree_min[2 * node], self.tree_min[2 * node + 1])
            self.tree_max[node] = max(self.tree_max[2 * node], self.tree_max[2 * node + 1])
    def _push(self, node):
        if self.lazy[node] != 0:
            lz = self.lazy[node]
            # Apply to children
            self.tree_min[2 * node] += lz
            self.tree_max[2 * node] += lz
            self.lazy[2 * node] += lz
            
            self.tree_min[2 * node + 1] += lz
            self.tree_max[2 * node + 1] += lz
            self.lazy[2 * node + 1] += lz
            
            self.lazy[node] = 0
    def _update(self, node, start, end, l, r, val):
        if l > end or r < start:
            return
        
        if l <= start and end <= r:
            self.tree_min[node] += val
            self.tree_max[node] += val
            self.lazy[node] += val
            return
            
        self._push(node)
        mid = (start + end) // 2
        self._update(2 * node, start, mid, l, r, val)
        self._update(2 * node + 1, mid + 1, end, l, r, val)
        
        self.tree_min[node] = min(self.tree_min[2 * node], self.tree_min[2 * node + 1])
        self.tree_max[node] = max(self.tree_max[2 * node], self.tree_max[2 * node + 1])
    def _find_last_zero(self, node, start, end, min_idx):
        if end < min_idx:
            return -1
            
        # Pruning: if 0 is impossible in this subtree
        if self.tree_min[node] > 0 or self.tree_max[node] < 0:
            return -1
            
        if start == end:
            return start if self.tree_min[node] == 0 else -1
            
        self._push(node)
        mid = (start + end) // 2
        
        # Priority to Right Child (We want Max R)
        res = self._find_last_zero(2 * node + 1, mid + 1, end, min_idx)
        if res != -1:
            return res
            
        return self._find_last_zero(2 * node, start, mid, min_idx)