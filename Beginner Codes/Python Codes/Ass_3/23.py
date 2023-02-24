# Input a number and print all the factors of that number (use loops).

number = int(input("Enter the number : "))
for i in range(1,number):
    if number%i==0:
        print(i)