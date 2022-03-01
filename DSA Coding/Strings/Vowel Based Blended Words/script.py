word1 = input()
word2 = input()
for char in word1:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vow1 = word1.find(char)
        vow2 = word2.find(char)
        break
blended_word = word1[0:vow1] + word2[vow2:]
print(blended_word)
