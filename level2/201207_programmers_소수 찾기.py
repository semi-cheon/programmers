# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.07.M
# 문제: 소수 찾기
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations 

def solution(numbers):
    candidates = []    
    
    for i in range(len(numbers)):
        temp_list = permutations(numbers, i+1)
        for j in temp_list :
            candidates.append(int("".join(j)))
    
    candidates = list(set(candidates))
    answer = len(candidates)
    for i in candidates :
        if i < 2 :
            answer -= 1
        for j in range(2, int(i**(1/2))+1):
            if i%j == 0 :
                answer -= 1
                break
    return answer

if __name__ == "__main__" :
    n_list = ['17', '011']

    for i in range(len(n_list)) :
        print(solution(n_list[i]))
        print("")
