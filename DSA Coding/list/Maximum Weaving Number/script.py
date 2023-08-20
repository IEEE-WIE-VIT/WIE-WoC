A = str(int(input()))
B = str(int(input()))
list1 = []
temp_str = ""
# Start from A
for counter in range(min(len(A), len(B))):
    temp_str = temp_str + A[counter] + B[counter]
    if (counter+1) == len(A):
        temp_str = temp_str + B[(counter + 1):]
        break
    elif (counter+1) == len(B):
        temp_str = temp_str + A[(counter + 1):]
        break
list1.append(int(temp_str))
temp_str = ''
# Start from B
for counter in range(min(len(A), len(B))):
    temp_str = temp_str + B[counter] + A[counter]
    if (counter+1) == len(A):
        temp_str = temp_str + B[(counter + 1):]
        break
    elif (counter+1) == len(B):
        temp_str = temp_str + A[(counter + 1):]
        break
list1.append(int(temp_str))
temp_str = ''
# End from A
for counter in range(min(len(A), len(B))):
    temp_str = temp_str + A[-(counter + 1)] + B[-(counter + 1)]
    if (counter+1) == len(A):
        temp_str = temp_str + B[-(counter +2): : -1]
        break
    elif (counter+1) == len(B):
        temp_str = temp_str + A[-(counter +2): : -1]
        break
list1.append(int(temp_str))
temp_str = ''
# End from B
for counter in range(min(len(A), len(B))):
    temp_str = temp_str + B[-(counter + 1)] + A[-(counter + 1)]
    if (counter+1) == len(A):
        temp_str = temp_str + B[-(counter +2): : -1]
        break
    elif (counter+1) == len(B):
        temp_str = temp_str + A[-(counter +2): : -1]
        break
list1.append(int(temp_str))
print(max(list1))

