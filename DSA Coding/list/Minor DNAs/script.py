from itertools import combinations
d = input()
k = int(input())
list1 = []
for counter in combinations(d, k):
    list1.append(''.join(counter))
list1.sort()
for counter in range(len(list1)):
    print(list1[counter])

