Number = int(input("Enter the number to check whether it is Adam's or not : "))
Quotient = Number
Square = Number ** 2
Sum = 0
while Quotient > 0:
    Remainder = Quotient % 10
    Sum = (Sum * 10) + Remainder
    Quotient //= 10
Quotient = Sum ** 2
Sum = 0
while Quotient > 0:
    Remainder = Quotient % 10
    Sum = (Sum * 10) + Remainder
    Quotient //= 10
if (Square == Sum):
    print(Number, "is an Adam's Number")
else:
    print(Number, "is not an Adam's Number")
