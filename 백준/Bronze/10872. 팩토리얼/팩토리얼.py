from functools import reduce

N = int(input())

answer = reduce(lambda x,y : x*y ,[i for i in range(1,N+1)], 1)
print(answer)