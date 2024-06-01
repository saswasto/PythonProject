from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            char = chars[read]
            count = 0
            while read < n and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
solution = Solution()

chars1 = ["a", "a", "b", "b", "c", "c", "c"]
new_length1 = solution.compress(chars1)
print(new_length1)  # Output: 6
print(chars1[:new_length1])  # Output: ['a', '2', 'b', '2', 'c', '3']

chars2 = ["a"]
new_length2 = solution.compress(chars2)
print(new_length2)  # Output: 1
print(chars2[:new_length2])  # Output: ['a']

chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
new_length3 = solution.compress(chars3)
print(new_length3)  # Output: 4
print(chars3[:new_length3])  # Output: ['a', 'b', '1', '2']
