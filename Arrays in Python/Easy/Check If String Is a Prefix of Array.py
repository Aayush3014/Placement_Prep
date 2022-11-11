s = "a"
words = ["aa","aaaa","banana"]
new_s = ""
for i in words:
    if i in s:
        new_s+= i
    else:
        # print(0)
        break
if new_s==s:
    print(1)
else:
    print(0)