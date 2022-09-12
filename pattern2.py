# n=int(input("enter no. "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     i=i+1
#     print()

n=int(input("enter the value of n:")) 
i=5
while i>=n:
    k=1
    while k<=5-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=i:
        print("*",end=" " )
        j=j+1
    # s=5
    # while s>(i-2):
    #     print(" ",end=" ")
    #     s=s-1
    i=i-1
    print()