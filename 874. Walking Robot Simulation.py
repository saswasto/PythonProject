#translated using AI
class Solution:
    def robotSim(self, commands, obstacles):
        obs = set()
        for x, y in obstacles:
            obs.add(f"{x},{y}")

        ch = 'N'
        x, y = 0, 0
        max_dist = 0

        for curr in commands:

            if curr == -1:
                if ch == 'N': ch = 'E'
                elif ch == 'E': ch = 'S'
                elif ch == 'S': ch = 'W'
                else: ch = 'N'

            elif curr == -2:
                if ch == 'N': ch = 'W'
                elif ch == 'W': ch = 'S'
                elif ch == 'S': ch = 'E'
                else: ch = 'N'

            else:
                if ch == 'N':
                    for _ in range(curr):
                        if f"{x},{y+1}" in obs:
                            break
                        y += 1

                elif ch == 'S':
                    for _ in range(curr):
                        if f"{x},{y-1}" in obs:
                            break
                        y -= 1

                elif ch == 'W':
                    for _ in range(curr):
                        if f"{x-1},{y}" in obs:
                            break
                        x -= 1

                elif ch == 'E':
                    for _ in range(curr):
                        if f"{x+1},{y}" in obs:
                            break
                        x += 1

                max_dist = max(max_dist, x*x + y*y)

        return max_dist