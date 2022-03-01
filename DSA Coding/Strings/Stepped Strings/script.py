s1 = input()
temp = s1.split(" ")
string1 = ""
for element in temp:
    string1 += element
s2 = input()
temp = s2.split(" ")
string2 = ""
for element in temp:
    string2 += element
Flag1 = True; Flag2 = True; Flag3 = False
for element1 in string1:
    if not element1.isalpha():
        Flag1 = False
        break
for element2 in string2:
    if not element2.isalpha():
        Flag2 = False
        break
if len(s1) != len(s2):
    print("Length different")
elif not Flag1 or not Flag2:
    print("Strings contain non alphabets")
elif s1.find(" ") != s2.find(" "):
    print("Strings differ in space")
else:
    for counter in range(len(string1)):
        if abs(ord(string1[counter]) - ord(string2[counter])) == (counter+1):
            Flag3 = True
        else:
            Flag3 = False
            break
    if not Flag3:
        print("Strings are not stepped")
    else:
        print("Strings are stepped")
