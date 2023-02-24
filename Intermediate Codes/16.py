from platform import python_branch
import string


# Reverse A String In python


# string = "ayush"
# reversed_string = string[::-1]
# print(reversed_string)

normal_string = "ayush"
reversed_string = ""
for i in range(len(normal_string)-1,-1,-1):
    reversed_string = reversed_string + normal_string[i]
print(reversed_string)