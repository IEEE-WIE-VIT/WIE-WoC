word = input()
occurence = 0
for temp_char in word:
    if (word.count(temp_char)) > occurence:
        occurence = word.count(temp_char)
        char = temp_char
position = []
temp_position = 0
for counter in range(0,occurence):
    position.append((word.find(char,temp_position)))
    temp_position = word.find(char,temp_position) + 1
print(char)
for counter in range(0,(occurence-1)):
    distance = position[counter+1] - position[counter]
    if distance == 1:
        print("No characters")
    elif distance == 2:
        print("1 character")
    else:
        print("%s characters" %(distance-1))

