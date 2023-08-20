n = int(input())
list1 = []
list2 = []
for row_counter in range(n):
    list1.append([])
    for column_counter in range(n):
        list1[row_counter].append(int(input()))
for column_counter in range(n):
    list2.append(list1[0][column_counter])
for row_counter in range(1,n):
    list2.append(list1[row_counter][n-1])
for column_counter in range((n-2), -1, -1):
    list2.append(list1[n-1][column_counter])
for row_counter in range((n-2), 0, -1):
    list2.append(list1[row_counter][0])
for counter in range(0, len(list2)-2, 2):
    x = list2[counter]
    y = list2[counter+2]
    list2.pop(counter)
    list2.insert(counter, y)
    list2.pop(counter+2)
    list2.insert(counter+2, x)
list2_counting = 0
for column_counter in range(n):
    list1[0][column_counter] = list2[list2_counting]
    list2_counting += 1
for row_counter in range(1,n):
    list1[row_counter][n-1] = list2[list2_counting]
    list2_counting += 1
for column_counter in range((n-2), -1, -1):
    list1[n-1][column_counter] = list2[list2_counting]
    list2_counting += 1
for row_counter in range((n-2), 0, -1):
    list1[row_counter][0] = list2[list2_counting]
    list2_counting += 1
for row_counter in range(n):
    for column_counter in range(n):
        print(list1[row_counter][column_counter], end="\t")
    print()
