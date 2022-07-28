def solution(x):
    a = [int(i) for i in str(x)]
    a = sum(a)
    if x % a == 0 :
        return True
    else : 
        return False