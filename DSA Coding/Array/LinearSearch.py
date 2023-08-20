#Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


n = int(input("Enter number: "))
arr = list(map(int, input().split()))
target = int(input("Enter target: "))
print(linear_search(arr, target))
