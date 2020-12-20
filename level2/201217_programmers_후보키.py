# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.17.T
# 문제: 후보키
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12985

from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    candi = []
    for i in range(1, col + 1) :
        candi += combinations(range(col), i)
        
    unique = []
    for c in candi :
        temp = [tuple([r[k] for k in c])  for r in relation]
        if len(set(temp)) == row :
            unique.append(c)
            
    answer = set(unique) 
    for i in range(len(unique)) :
        for j in range(i+1, len(unique)) :
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                if unique[j] in answer :
                    answer.remove(unique[j])
    return len(answer)

if __name__ == "__main__" :  
    
    # for i in range(len(n)) :
    print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
    print("")

    