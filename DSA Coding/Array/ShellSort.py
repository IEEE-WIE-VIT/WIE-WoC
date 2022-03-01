# Shell Sort

def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j] < arr[j - gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap //= 2
    return arr

n = int(input("Enter number: "))
arr = list(map(int, input().split()))
print(*shellSort(arr))