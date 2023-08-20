x = int(input())
if ((x % 6) == 1) or ((x % 6) == 0):
    color = "Green"
elif ((x % 6) == 2) or ((x % 6) == 5):
    color = "Orange"
elif ((x % 6) == 3) or ((x % 6) == 4):
    color = "Blue"
if (x % 12) <= 6:
    y = 12*((x//12)+1) - (x % 12) + 1
else:
    y = 12*((x//12)+1) - (x % 12) + 1
print(y)
print(color)
