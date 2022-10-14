gain = [-4,-3,-2,-1,4,3,2]
# new=[]
greater = 0
sum = 0
# new.append(sum)
for i in range(len(gain)):
    sum+=gain[i]
    if sum>greater:
        greater = sum
    # new.append(sum)
print(greater)


# Or we can also use a variable for storing the greater variable.

