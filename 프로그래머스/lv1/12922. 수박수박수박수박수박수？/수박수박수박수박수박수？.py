def solution(n):
    for i in range(n+1):
      if i == n :
        answer = '수박'*i
        answer = answer[:i]
        return answer