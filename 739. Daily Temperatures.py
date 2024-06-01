from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)

        return answer
# Example 1
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
solution = Solution()
print(solution.dailyTemperatures(temperatures))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]

# Example 2
temperatures = [30, 40, 50, 60]
print(solution.dailyTemperatures(temperatures))  # Output: [1, 1, 1, 0]

# Example 3
temperatures = [30, 60, 90]
print(solution.dailyTemperatures(temperatures))  # Output: [1, 1, 0]
