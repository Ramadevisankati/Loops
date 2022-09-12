# for i in range(6):
#     for j in range(7):
#         if (i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()
    
# for row in range(7):
#     for col in range(5):
#         if ((col==0 or col==4) and (row!=0)) or ((row==0 or row==3 )and (col>0 and col<4)) :
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# for row in range(5):
#     for col in range(4):
#         if ((row==0 or row==4) or col==0 ) or ((col>0 and col<3) and row==2) or ((row==1 or row==3) and col>2):
            
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()


# for row in range(5):
#     for col in range(5):
#         if (col+row==4 or row-col==0):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# for row in range(5):
#     for col in range(4):
#         if (row==0 or col==0)or (row+col==4 and row!=3) or (row-col==1):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
    
# for row in range(5):
#     for col in range(3):
#         if (row==0 or col==0 and row!=4) or (row==2 or row==3) or row-col==2:
#             print("*",end=" ")
#         else:
#             print(end="")
#     print()

for row in range(5):
    for col in range(4):
        if (col==0 or (col<2 and row==2)):
            print("*",end="")
        else:
            print(end="")
    print()