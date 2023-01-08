garbage = ["MMM","PGM","GP"]
travel = [3,10]
m = 0
p = 0
g = 0
t = 0
for i in range(len(garbage)):
    if i>0:
        t += travel[i-1]
    if "M" in garbage[i]:
        m += garbage[i].count("M")
    # t += travel[i]
print(t+m)