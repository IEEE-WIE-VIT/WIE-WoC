def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
d=gcd(n1,n2)
print("GCD of",n1,"and",n2,"is:",d)
