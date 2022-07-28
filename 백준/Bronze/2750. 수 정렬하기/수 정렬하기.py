n = int(input())

num1 = []
for i in range(n) :
    num = int(input())
    num1.append(num)
num1.sort()
for i in range(n):
    print(num1[i])