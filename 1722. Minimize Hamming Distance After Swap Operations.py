from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        parent = list(range(len(source)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for a, b in allowedSwaps:
            union(a, b)

        groups = defaultdict(list)
        for i in range(len(source)):
            groups[find(i)].append(i)

        res = 0
        for group in groups.values():
            count = Counter()
            
            for i in group:
                count[source[i]] += 1
            
            for i in group:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    res += 1

        return res