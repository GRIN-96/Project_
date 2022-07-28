def solution(s):
    ss=s.lower()
    a=ss.count('p')
    b =ss.count('y')
    if a == b : 
        return True
    elif a != b :
        return False