class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # -------- single character runs --------
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            ans = max(ans, j - i)
            i = j
        
        # -------- two-character balance --------
        def check_pair(x, y):
            nonlocal ans
            i = 0
            while i < n:
                if s[i] not in (x, y):
                    i += 1
                    continue
                j = i
                while j < n and s[j] in (x, y):
                    j += 1
                
                diff = 0
                first = {0: i - 1}
                for k in range(i, j):
                    diff += 1 if s[k] == x else -1
                    if diff in first:
                        ans = max(ans, k - first[diff])
                    else:
                        first[diff] = k
                i = j
        
        check_pair('a', 'b')
        check_pair('a', 'c')
        check_pair('b', 'c')
        
        # -------- three-character balance --------
        ca = cb = cc = 0
        first = {(0, 0): -1}
        for i, ch in enumerate(s):
            if ch == 'a':
                ca += 1
            elif ch == 'b':
                cb += 1
            else:
                cc += 1
            
            key = (ca - cb, ca - cc)
            if key in first:
                ans = max(ans, i - first[key])
            else:
                first[key] = i
        
        return ans
