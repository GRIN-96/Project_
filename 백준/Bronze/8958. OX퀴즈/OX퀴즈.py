n= int(input())

for i in range(n):
    a = input()
    b = list(a)
    sum=0
    count1=0
    for j in b :
        if j == 'O' :
            count1 += 1
        else : 
            count1 = 0
        sum += count1
    print(sum)