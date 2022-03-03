def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
print("enter positive numbers below")
num=int(input("enter base number:"))
p=int(input("raised to power of:"))
result=power(num,p)
print(num,"raised to power of",p,"is",result)
