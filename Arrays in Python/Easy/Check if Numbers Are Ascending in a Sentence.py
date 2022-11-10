s = "hello world 5 x 5"
result = True
current_num = -1
for i in s.split(" "):
    if i.isdigit():
        if int(i)<=current_num:
            result = False
            break
        else:
            current_num = int(i)
print(result)

