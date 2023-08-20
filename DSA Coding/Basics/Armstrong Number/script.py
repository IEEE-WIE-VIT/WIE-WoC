Number = int(input("Enter the number to check whether it is Armstrong or not : "))
Quotient = Number
Sum = 0
while Quotient > 0:
    Remainder = Quotient % 10
    Sum = Sum + (Remainder**3)
    Quotient //= 10
if (Sum==Number):
    print(Number, "is an Armstrong Number")
else:
    print(Number, "is not an Armstrong Number")