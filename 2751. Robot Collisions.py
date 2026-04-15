class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        
        robots = sorted(
            [(positions[i], healths[i], directions[i], i) for i in range(n)]
        )
        
        stack = []
        alive = [True] * n
        
        for pos, health, dirc, idx in robots:
            
            if dirc == 'R':
                stack.append(idx)
            else:
                while stack and alive[idx]:
                    top = stack[-1]
                    
                    if not alive[top]:
                        stack.pop()
                        continue
                    
                    if healths[top] < healths[idx]:
                        alive[top] = False
                        stack.pop()
                        healths[idx] -= 1
                    
                    elif healths[top] > healths[idx]:
                        alive[idx] = False
                        healths[top] -= 1
                        break
                    
                    else:
                        alive[top] = False
                        alive[idx] = False
                        stack.pop()
                        break
        
        result = []
        for i in range(n):
            if alive[i]:
                result.append(healths[i])
        
        return result