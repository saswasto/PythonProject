class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return next((c for c in letters if c > target), letters[0])