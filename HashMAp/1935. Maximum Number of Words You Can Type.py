text = "leet code"
brokenLetters = "lt"
count = 0
text = text.split(" ")
for i in text:
    for j in brokenLetters:
        if j not in i:
            count+=1
            break
print(count)