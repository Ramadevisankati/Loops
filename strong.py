n=int(input("enter no.: "))
s=0
temp=n
while n>0:
    f=1
    i=1
    rem=n%10
    while i<=rem:
        f=f*i
        i=i+1
    s=s+f
    n=n//10
if s==temp:
    print("strong number")
else:
    print("not strong")