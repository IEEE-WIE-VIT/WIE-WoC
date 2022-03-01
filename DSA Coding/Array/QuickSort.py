# Quiz Sort

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)


n = int(input("Enter number: "))
arr = list(map(int, input().split()))
print(*quickSort(arr))
