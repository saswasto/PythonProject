import math

class Solution:
    def pivointeger(self, n: int) -> int:
        y = (n * n + 2) // 2
        x = int(math.sqrt(y))
        return x if x * x == y else -1
