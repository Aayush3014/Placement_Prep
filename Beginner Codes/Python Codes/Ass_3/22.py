# Leetcode

# Subtract the Product and Sum of Digits of an Integer 

number = 345
prod = 1
sum = 0
while number>0:
    d = number % 10
    sum = sum + d
    prod = prod*d
    number = number//10
print(prod-sum)