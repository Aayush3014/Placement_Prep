candies = [2,3,5,1,3]
extraCandies = 3
new_arr = []
greater = 0

for i in range(len(candies)):
    if candies[i]>greater:
        greater = candies[i]
    new_arr.append(candies[i]+extraCandies)
for i in range(len(new_arr)):
    if new_arr[i]>= greater:
        new_arr[i] = "true"
    else:
        new_arr[i] = "false"
print(new_arr)

    
#     for j in range(n):
#         sum += accounts[i][j]
#     sum_list.append(sum)

# for i in sum_list:
#     if i>greater:
#         greater = i
# print(greater)