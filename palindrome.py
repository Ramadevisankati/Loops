num =int(input("number"))
reverse = 0
number = num
while(num>0):
   remainder = num % 10
   reverse = reverse * 10 + remainder
   num = int(num / 10)
if(number == reverse):
   print(number,'is a Palindrome')
else:
   print(number,'is not a Palindrome')
   