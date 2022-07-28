n = int(input())

num = list(map(int,input().split()))
c = 0
for i in num:
    b=0
    if i>1 :
        for j in range(2,i+1) :
            if i % j == 0 :
                b += 1
        if b == 1 : 
            c+=1  

print(c)