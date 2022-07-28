n = int(input())
i = n 
sum2 = 0
count = 0
sum1 =0
while True :
	sum1= (n//10)+(n%10)
	sum2 = (n%10)*10 + (sum1%10)
	count += 1
	n = sum2
	if sum2 == i :
		break
print(count)