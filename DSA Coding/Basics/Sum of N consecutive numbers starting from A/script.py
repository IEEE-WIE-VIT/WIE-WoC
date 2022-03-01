Start_Number = int(input("Enter the starting number : "))
Number = int(input("Enter how many consecutive terms you want to add : "))
Temp_Store = Start_Number
counter = 1
while (counter < Number):
    counter += 1
    Temp_Store += 1
    Start_Number += Temp_Store
print("Sum :", Start_Number)
