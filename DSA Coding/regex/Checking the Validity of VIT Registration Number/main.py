import re
Reg_no = input("Enter your Registration Number : ")
if re.match("^[^0][0-9][A-Za-z]{3}[0-9]{4}$",Reg_no.strip()):
    print("{} is a valid Registration Number".format(Reg_no))
else:
    print("%s is an invalid Registration Number" %Reg_no)

