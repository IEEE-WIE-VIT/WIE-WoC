import math
print("The format of the quadratic equation is : \n"
      "ax^2 + bx + c = 0 \n"
      "where, a is not equal to 0")
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = float(input("Enter the value of c : "))
D = (b**2) - (4 * a * c) # D = Discriminant
eq = "(" + str(a) + ")x**2 + " + str(b) + "x + " + str(c) + " = 0"
if (D < 0):
    print("There are no real solutions for the equation : ", eq, "\n"
          "Therefore, the imaginary solutions are : \n"
          "X1 = ", (-b/(2*a)), "+ i", (math.sqrt(abs(D))/(2*a)), "\n"
          "X2 = ", (-b/(2*a)), "- i", (math.sqrt(abs(D))/(2*a)))
elif (D==0):
    x1 = ((-b) - math.sqrt(D)) / (2 * a)
    print("The solutions for the equation :", eq, "are", x1, "and", x1)
else:
    x1 = ((-b) - math.sqrt(D)) / (2 * a)
    x2 = ((-b) + math.sqrt(D)) / (2 * a)
    print("The solutions for the equation :", eq, "are", x1, "and", x2)
