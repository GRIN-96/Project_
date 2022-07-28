import math

def solution(n):    
    a=math.sqrt(n)
    if int(a)==a:
        return (a+1)**2
    else:
        return -1
