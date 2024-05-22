def twoSumHashing(arr, target):
    sums = []
    hashTable = {}

    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in hashTable:
            print("Target value with sum ", target, "is: (", arr[i], ",", complement, ")")
        hashTable[arr[i]] = arr[i]


arr = [2,5,6,8,11]
target = 14

twoSumHashing(arr, target)

