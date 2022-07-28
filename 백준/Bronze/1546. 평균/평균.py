n = int(input())
num = list(map(int,input().split()))
num1 = max(num)
num2 = [i/num1*100 for i in num]
num3 = sum(num2)/n

print(num3)