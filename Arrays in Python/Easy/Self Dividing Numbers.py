left = 1
right = 22
ans = []
# for i in range(len(str()))
def self_divide(n):
    for k in str(n):
        if k=='0' or n % int(k)>0:
            return False
    return True
for i in range(left,right+1):
    if self_divide(i):
        ans.append(i)
print(ans)

# def divisible(n):
#             for d in str(n):
#                 if d == '0' or n % int(d) > 0:
#                     return False
#             return True
        
#         res = []
#         for n in range(left, right + 1):
#             if divisible(n):
#                 res.append(n)
#         return res