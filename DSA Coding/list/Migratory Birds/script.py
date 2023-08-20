n = int(input())
ar = list(map(int, input().split(" ")))


def migratoryBirds(arr):
    typecount = [0 for i in range(5)]
    for i in arr:
        typecount[i-1] += 1
    max_count = max(typecount)
    for i in range(5):
        if typecount[i] == max_count:
            return i+1

print(migratoryBirds(ar))
