n=int(input("enter no.: "))
p=n
sum1=0
while n>0:
    s=sum1+n%10
    n=n//10
if p%s==0:
    print("harshad number")
else:
    print("not a harshad number")

