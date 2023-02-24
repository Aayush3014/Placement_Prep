# to find the armstrong number.
number = int(input("Enter the number : "))
count = 0
sum = 0
n1 = number
n2 = number
while number>0:
    number = number//10
    count += 1
while n1>0:
    d = n1%10
    sum = sum + d**count
    n1=n1//10
if sum == n2 :
    print("The number is armstrong number.")
else:
    print("The number is not an armstrong number.")