# Take integer inputs till the user enters 0 and print the largest number from all.
ans = "yes"
largest = 0
while ans=="yes":
    number = int(input("Enter the number : "))
    if number!=0:
        if number>largest:
            largest = number
    else:
        print(largest)
        break
    ans = input("Want to enter new number ? (yes/no)")
