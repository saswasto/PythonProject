class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        perimeter = 4 * side
        pos = []
        for x, y in points:
            if y == 0:
                pos.append(x)  
            elif x == side:
                pos.append(side + y)  
            elif y == side:
                pos.append(3 * side - x)  
            else:
                pos.append(4 * side - y)  

        pos.sort()
        n = len(pos)

        arr = pos + [x + perimeter for x in pos]

        def can_pick(dist):
            for start in range(n):
                count = 1
                first = arr[start]
                last = first
                idx = start

                while count < k:
                    target = last + dist

                    left = idx + 1
                    right = start + n

                    while left < right:
                        mid = (left + right) // 2
                        if arr[mid] >= target:
                            right = mid
                        else:
                            left = mid + 1

                    if left >= start + n:
                        break

                    last = arr[left]
                    idx = left
                    count += 1

                if count == k:
                    gap = perimeter - (last - first)
                    if gap >= dist:
                        return True

            return False

        left, right = 0, 2 * side
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if can_pick(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans