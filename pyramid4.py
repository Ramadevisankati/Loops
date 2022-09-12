n=int(input("enter the n value: "))
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j=j+1
    k=1
    while k<=i:
        print(i,end=" ")
        k=k+1
    i=i+1
    print()
