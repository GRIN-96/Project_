def solution(arr, divisor):
    answer = [i for i in arr if i%divisor == 0]
    answer.sort()
    if answer : 
        return answer
    else  : 
        return [-1]