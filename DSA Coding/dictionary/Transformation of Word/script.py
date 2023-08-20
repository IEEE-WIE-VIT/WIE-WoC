s = input()
s_new = ""
l = []
dic = {}
for counter in range(len(s)):
    d = int(input())
    l.append([s[counter], d])
    dic[s[counter]] = counter+1
for i in range(len(l)):
    small = i
    for j in range(i + 1, len(l)):
        if l[small][1] > l[j][1]:
            small = j
    l[i], l[small] = l[small], l[i]
for counter in range(len(l)):
    s_new += l[counter][0]
print(s_new)
for counter in range(len(s_new)):
    print(dic[s_new[counter]])
