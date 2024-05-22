from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int, path: List[str]):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
        result = []
        backtrack(0, [])
        return result
# Example give me by leetcode :
s1 = "aab"
s2 = "a"

solution = Solution()
print(solution.partition(s1))  # Output for example 1 are given: [["a","a","b"],["aa","b"]]
print(solution.partition(s2))  # Output for example 2 are given: [["a"]]

