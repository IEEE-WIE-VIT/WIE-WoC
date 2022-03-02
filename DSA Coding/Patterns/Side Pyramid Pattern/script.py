Height = int(input("Enter the Height of the pyramid pattern : "))
if Height < 0:
    print("Invalid Input")
elif Height == 0 :
    print()
else:
    for row_counter in range(1, Height+1):
        for column_counter in range(1, row_counter+1):
            print("*", end=" ")
        print()
    for row_counter in range(1, Height+1):
        for column_counter in range(Height-row_counter, 0, -1):
            print("*", end=" ")
        print()
