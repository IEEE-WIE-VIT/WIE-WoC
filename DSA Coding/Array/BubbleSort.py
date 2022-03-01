#Bubble Sort 

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

n = int(input("Enter number: "))
arr = list(map(int, input().split()))
print(*bubbleSort(arr))