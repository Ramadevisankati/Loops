# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range (n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()
    
# n=int(input("enter the number:"))
# for i in range (n):
#     for j in range(n-i-1):
#         print("",end=" ")
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()                        
 
 
# n=int(input("enter the number: "))   
# for i in range(n-1,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()

n=int(input("enter number:"))
k=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()