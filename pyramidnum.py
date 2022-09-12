n=int(input("enter the number; "))
i=1
while i<=n:
    a=1
    while a<=n-i:
        print(" ",end=" ") #print(" ",end="")
        a=a+1
    j=1
    while j<=i:

        print(j,end=" ")
        j=j+1
    print( )
    i=i+1
