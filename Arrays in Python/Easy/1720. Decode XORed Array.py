output = []
encoded = [6,2,7,3]
first = 4
output.append(first)
# op = [4,2,0,7,4]
for i in encoded:
    res = first^i
    output.append(res)
    first = res
print(output)