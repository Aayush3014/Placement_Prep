

accounts = [[1,2,3],[1,2,3]]
sum_list = []
sum = 0
greater = 0
m = len(accounts)

for i in range(m):
    sum = 0
    n = len(accounts[i])
    for j in range(n):
        sum += accounts[i][j]
    sum_list.append(sum)

for i in sum_list:
    if i>greater:
        greater = i
print(greater)