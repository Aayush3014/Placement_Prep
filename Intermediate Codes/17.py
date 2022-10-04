# Find if a number is palindrome or not


number = int(input("Enter the number : "))
sum = 0
n1,n2=number,number
while number>0:
    rem = number%10
    sum = sum*10+rem
    number = number //10
if n1 == sum:
    print("It is palindrome.")
else:
    print("It is not palindrome.")