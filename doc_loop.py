  
# i=1
# while i<=10:
#     print(i,i*i)
#     i=i+1

# i=105
# while i>=7:
#     if i%7==0:
#        print(i)
#        i=i-7

# i=10
# while i<=300:
#     print(i)
#     i=i+10

# i=0
# a=0
# while i<=10:
#     a=a+i
#     i=i+2
# print(a)
    
# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# while num1<=num2:
#     if num1%2==0:
#         print(num1)
#     num1=num1+1

# n=int(input("enter the number:"))
# sum=0
# i=n
# while n>0:
#     a=n%10
#     sum=sum+a
#     n=n//10
# print("sum of the digits are",sum)

# n=int(input("enter the num:"))
# p=1
# while n>0:
#     p=p*(n%10)
#     n=n//10
# print("product of the number",p)

n=int(input("enter the number "))
r=0
while n>0:
    r=(r*10)+n%10
    n=n//10
print("reverse number is",r)

# i=1
# max=0
# min=1000
# while i<=5:
#     user=int(input("enter numbers "))
#     if user>max:
#         max=user
#     i=i+1
#     if user<min:
#         min=user
#     i=i+1
# print(max,"is max")
# print(min,"is min")