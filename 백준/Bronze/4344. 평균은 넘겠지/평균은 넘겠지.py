n = int(input())

for i in range(n) :
    a = list(map(int,input().split()))
    b = sum(a[1:])/a[0]
    count = 0
    for score in a[1:] :
        if score > b :
            count += 1
    c = count/a[0]*100
    print(f'{c:.3f}%')