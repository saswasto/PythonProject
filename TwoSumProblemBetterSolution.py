def twoSumNaive(arr, target):
    for i in range(len(arr)-1):
        for j in range (i+1, len(arr)):
            if arr[i] + arr[j] == target:
                print("target value with sum ", target, "is: (", arr[i], ",", arr[j], ")")

arr = [2,5,6,8,11]
target= 14
twoSumNaive(arr,target)
