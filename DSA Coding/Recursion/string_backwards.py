def bg(sg,n):
    if n>0:
        print(sg[n],end=' ')
        bg(sg,n-1)
    elif n==0:
        print(sg[0])
s=input("enter a string")
bg(s,len(s)-1)
