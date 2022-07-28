def solution(n):
    a = []
    for i in range(1,n+1):
        if n%i == 0 :
            a.append(i)
    a = sum(a)
    return a


