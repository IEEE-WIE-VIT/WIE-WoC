import re
Email = input("Enter your Email Address : ")
if re.match("^[A-Za-z][A-Za-z0-9]*[@][a-z]+[\.][a-z]+$",Email.strip()):
    print("{} is a valid Email Address".format(Email))
else:
    print("%s is an invalid Email Address" %Email)
