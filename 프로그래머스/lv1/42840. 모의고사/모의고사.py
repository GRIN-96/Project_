def solution(answers):
    su1 = [1,2,3,4,5]
    su2 = [2,1,2,3,2,4,2,5]
    su3 = [3,3,1,1,2,2,4,4,5,5]
    count=[0,0,0]
    best = []
    for i in range(len(answers))  :
        if answers[i] == su1[i%len(su1)]:
            count[0]+=1
        if answers[i] == su2[i % len(su2)] :
            count[1]+=1
        if answers[i] == su3[i % len(su3)] :
            count[2]+=1

    max_co = max(count)

    for i in range(3):
        if max_co == count[i] :
            best.append(i+1)

    return best