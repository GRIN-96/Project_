def solution(n, m):
    answer1 = [i for i in range(1,n+1) if n%i == 0]
    answer2 = [i for i in range(1,m+1) if m%i == 0]
    answer = set(answer1) & set(answer2)
    answer = list(answer)
    a = max(answer) #최대공약수
    li1 = [i for i in range(n,n*m+1,n)]
    li2 = [i for i in range(m,n*m+1,m)]
    answer1 = set(li1) & set(li2)
    answer2 = list(answer1)
    b = min(answer2)
    return [a,b]