# n=int(input("enter the number: "))
# i=0
# # k=i+1
# while i<=n:
#     k=1+i
#     j=0
#     while j<=i:
#         print(k,end=" ")
#         j=j+1
#         k=k+1
#     i=i+1
#     print()
    
n=int(input("enter the number:"))
i=1
while i<=n:
    j=1
    while j<=i:
        if j%2!=0:
            print(i,end=" ")
        else:
            print("*",end=" ")
        j=j+1
    i=i+1
    print()
        
        
# n=0
# i=5
# while i>=n:
#     k=1+i
#     j=0
#     while j<=i:
#         print(k,end=" ")
#         k=k+1
#         j=j+1
#     i=i-1
#     print(6)
