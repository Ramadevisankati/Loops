# i=1
# count=0
# num=int(input("enter the number"))
# while i<=num:
#     if num%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print("prime number")
# else:
#     print("not a prime number")
    
    
n=int(input("enter the number: "))
i=1
while i<=n:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count=count+1
        j=j+1
    if count==2:
        print(i)
    i=i+1