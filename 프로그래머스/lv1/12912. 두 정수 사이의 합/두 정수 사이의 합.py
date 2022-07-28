import random
import os

def solution(a, b) :
    num = [a,b]
    num.sort()
    answer = 0
    if a != b :
        for i in range(num[0],num[1]+1) : 
                answer += i
        return answer
    elif a == b :
        answer = random.choice(num)
        return answer