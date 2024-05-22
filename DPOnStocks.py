def maximum_profit(arr):
    max_profit = 0
    mini = arr[0]

    for i in range(1, len(arr)):
        cur_profit = arr[i] - mini
        max_profit = max(max_profit, cur_profit)
        mini = min(mini, arr[i])

    return max_profit


if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    print("The maximum profit by selling the stock is", maximum_profit(arr))
