num = int(input("enter the binary value: "))
a = 0
i = 1
while num>0:
    r = num%10
    a = a + (r*i)
    i = i*2
    num = int(num/10)
print("Value = ", a)
