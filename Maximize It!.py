K, M = map(int, input().split())

lists = []
for _ in range(K):
    arr = list(map(int, input().split()))
    Li = arr[0]
    nums = arr[1:]
    # Store squared values modulo M
    lists.append([ (x * x) % M for x in nums ])

# Start with sum = 0 before choosing anything
possible = {0}

for lst in lists:
    new_possible = set()
    for prev in possible:
        for val in lst:
            new_possible.add((prev + val) % M)
    possible = new_possible  
# move to next stage

# We want the maximum modulo result
print(max(possible))