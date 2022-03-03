def maximum(a, b, c):
  
    if (a >= b) and (a >= c):
        largest = a
  
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
          
    return largest
  
  
# Driven code 
a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
print("The largest number among the three is ",maximum(a, b, c))
