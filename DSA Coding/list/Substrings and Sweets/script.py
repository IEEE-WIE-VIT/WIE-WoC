w = input()
k = int(input())
s = []
l = []
for substring_length in range(1, len(w)+1):
    for start_letter in range(len(w)+1-substring_length):
        s.append(w[start_letter:(start_letter+substring_length)])
for word in s:
    counting = 0
    for letter in word:
        if letter in ["a", "e", "i", "o", "u"]:
            counting += 1
    if counting == k:
        l.append(word)
print(l)
