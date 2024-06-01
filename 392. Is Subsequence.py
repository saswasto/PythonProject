class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
solution = Solution()

# Example 1
s1 = "abc"
t1 = "ahbgdc"
print(solution.isSubsequence(s1, t1))  # Output: True

# Example 2
s2 = "axc"
t2 = "ahbgdc"
print(solution.isSubsequence(s2, t2))  # Output: False
