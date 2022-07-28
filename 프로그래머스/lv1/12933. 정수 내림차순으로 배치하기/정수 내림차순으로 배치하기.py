def solution(n):
    a = str(n)
    aa = [int(i) for i in a]
    aa.sort()
    aaa= aa[::-1]
    b = [str(i) for i in aaa]
    c = ''.join(b)
    return int(c)