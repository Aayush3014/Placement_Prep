######review


s = "is2 sentence4 This1 a3"
lst = []
s = s.split(" ")
for i in s:
    word = i[-1]
    lst.append(word)
lst.sort()
print("".join(lst))