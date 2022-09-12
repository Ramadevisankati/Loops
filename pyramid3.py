# num=int(input("enter a number)"))
# i=1
# while i<=num:
#     j=1
#     while j<=num:
#         print(j,end=" ")
#         j=j+1
#     i=i+1
#     print()



n=int(input("enter the number: "))
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j=j+1
    k=1
    while k<=i:
        print("*",end=" ")
        k=k+1
    i=i+1
    print()

n=int(input("enter num: "))
i=5
while i>=1:
    j=5
    while j>=n-i:
        print(" ",end=" ")
        j=j-1
    k=5
    while k>=i:
        print("*",end=" ")   
        k=k-1
    i=i-1
    print()
        
