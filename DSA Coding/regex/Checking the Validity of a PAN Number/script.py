import re
PAN_Number = input("Enter a PAN Number : ")
if re.match('^[a-zA-z]{5}[0-9]{4}[a-zA-z]$',PAN_Number.strip()):
    print("{} is a valid PAN Number".format(PAN_Number))
else:
    print("%s is an invalid PAN Number" %PAN_Number)