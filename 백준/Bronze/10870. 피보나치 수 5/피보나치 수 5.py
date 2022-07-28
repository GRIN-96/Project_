n = int(input())


li1 = [0,1]
a = 0
for i in range(n):
    a=li1[i]+li1[i+1]
    li1.append(a)
print(li1[n])