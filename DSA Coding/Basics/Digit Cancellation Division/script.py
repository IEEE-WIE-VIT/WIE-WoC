x = list(str(int(input())))
y = list(str(int(input())))
num = 1
denom = 1
div = 1
if int("".join(y))==0:
    num = -1
    denom = 1
else:
    counter = 0
    while counter < len(x):
        if x[counter] in y:
            pos_x = x.index(x[counter])
            pos_y = y.index(x[counter])
            x.pop(pos_x)
            y.pop(pos_y)
        else:
            counter += 1
    if x==[]:
        x = ["1"]
    if list(map(int, y))==[0]:
        x = ["-1"]
        y = ["1"]
    if y==[]:
        y = ["1"]
    num = int("".join(x))
    denom = int("".join(y))
div = num/denom
print(format(div, ".2f"))

