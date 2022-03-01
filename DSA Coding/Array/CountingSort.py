# Counting Sort

def countingSort(arr):
    max_val = max(arr)
    min_val = min(arr)
    count = [0] * (max_val - min_val + 1)
    for i in arr:
        count[i - min_val] += 1
    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i + min_val
            index += 1
            count[i] -= 1
    return arr

n = int(input("Enter number: "))
arr = list(map(int, input().split()))
print(*countingSort(arr))
