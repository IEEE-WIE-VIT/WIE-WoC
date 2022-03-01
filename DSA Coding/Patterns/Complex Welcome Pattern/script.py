temp = list(map(int, input().split(" ")))
n = temp[0]
m = temp[1]
for row_counter in range(n // 2):
    for column_counter1 in range(((m - 1) // 2) - (3 * row_counter + 1)):
        print("-", end="")
    for counter_counter2 in range(2 * row_counter + 1):
        print(".|.", end="")
    for column_counter3 in range(((m - 1) // 2) - (3 * row_counter + 1)):
        print("-", end="")
    print()
for counter in range((m-7)//2):
    print("-", end="")
print("WELCOME", end="")
for counter in range((m-7)//2):
    print("-", end="")
print()
for row_counter in range(n // 2):
    for column_counter1 in range(3*(row_counter+1)):
        print("-", end="")
    for counter_counter2 in range(n - (2 * row_counter + 2)):
        print(".|.", end="")
    for column_counter3 in range(3*(row_counter+1)):
        print("-", end="")
    print()
