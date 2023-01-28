# 633. Sum of Square Numbers

c = 3
i,j = 0,1
ans = False
while j<c:
	if ((i**2)+(j**2))==c:
		ans = True
		break
	else:
		i+=1
		j+=1
print(ans)