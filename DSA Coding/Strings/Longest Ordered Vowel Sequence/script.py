line = input().split()
unique = []
unique_count = 0
for word in line:
    Flag = False
    prev_letter = ''
    for letter in word:
        if letter in "aeiou":
            if prev_letter <= letter:
                Flag = True
                prev_letter = letter
            else:
                Flag = False
                break
        else:
            continue
    if Flag:
        check = []
        for letter in word:
            if letter in "aeiou" and letter not in check:
                check.append(letter)
        if unique_count < len(check):
            unique = [word]
            unique_count = len(check)
        elif unique_count == len(check):
            unique.append(word)
for word in unique:
    print(word)
