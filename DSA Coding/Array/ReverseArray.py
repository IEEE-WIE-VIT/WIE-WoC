#Reverse Array
#Given an array, reverse the order of the elements.

def reverseArray(arr):
    return arr[::-1]

n = int(input("Enter number: "))
arr = list(map(int, input().split()))
print(*reverseArray(arr))