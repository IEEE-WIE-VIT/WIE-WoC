n = int(input())
list1 = []
for counter in range(n):
    temp = input().split()
    list1.append([int(temp[0]), int(temp[1])])
check_point = int(input())
temp_check_point = check_point
counting = 0
for counter1 in range(n):
    if counting != 0:
        if check_point == temp_check_point:
            break
    for counter2 in range(n):
        if list1[counter2][0] == temp_check_point:
            temp_check_point = list1[counter2][1]
            counting += 1
        if counting != 0:
            if check_point == temp_check_point:
                break
if temp_check_point != check_point:
    print(0)
else:
    print(counting)

