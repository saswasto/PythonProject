def lenOfLongSubarr(arr, N, K):
    maxlength = 0
    for i in range(0, N):
        Sum = 0
        for j in range(i, N):
            Sum += arr[j]
            if Sum == K:
                maxlength = max(maxlength, j - i + 1)
    return maxlength

arr = [1,2,3,1,1,1,1,3,3]
N = len(arr)
K = 6
print("Length =", lenOfLongSubarr(arr, N, K))
