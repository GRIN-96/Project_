num = set(range(1,10001))
num1 = set()

for i in range(1,10001):
    for j in str(i):
        i+= int(j)
    num1.add(i)

self_num = sorted(num - num1)

for i in self_num:
    print(i)
