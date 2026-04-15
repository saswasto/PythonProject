class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return sum((c=='L')-(c=='R')+(((c=='U')-(c=='D'))<<15) for c in moves)==0
        