S = input().lower()
line = S
list1 = []
counter = 0
if 1 <= len(S) <= 50:
    for i in range(len(S)):
        line = line[-1] + line[0:-1]
        if line not in list1:
            counter += 1
            list1.append(line)
    print(counter)
