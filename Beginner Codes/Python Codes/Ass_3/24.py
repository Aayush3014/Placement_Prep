# Take integer inputs till the user enters 0 and print the sum of all numbers (HINT: while loop)
ans = "yes"
sum = 0
while ans=="yes":
    number = int(input("Enter the number : "))
    if number!=0:
        sum+=number
    else:
        print(sum)
        break
    ans = input("Want to enter new number ? (yes/no)")
