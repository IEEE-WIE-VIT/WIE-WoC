PhoneNumber = (input("Enter the Phone Number : "))
if len(PhoneNumber) != 10:
    print("The Phone number is not of 10 digits")
elif PhoneNumber[0] == '0':
    print("The Phone number shouldn't start with a 0")
else:
    print("%s is a valid Phone Number" %PhoneNumber)