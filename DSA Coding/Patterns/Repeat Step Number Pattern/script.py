Height = int(input("Enter the height of the pattern : "))
if Height < 0:
    print("Invalid Input")
elif Height == 0:
    print()
else:
    for row_counter in range(1,Height+1): 
        for column_counter in range((Height + 1) - row_counter,0,-1):
            print(row_counter, end=" ")
        print()
