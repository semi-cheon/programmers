# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.14.M
# 문제: 소수 만들기
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations 

def check(t): 
    for i in range(2, t): 
        if t % i == 0 : return False 
    return True 

def solution(nums):
    answer = 0 
    target_nums = [sum(c) for c in combinations(nums, 3)]
    
    for t in target_nums :
        if check(t) :
            answer += 1    
    return answer
    
if __name__ == "__main__" :
    s_list = [[1,2,3,4]
            , [1,2,7,6,4]]
    
    for i in range(len(s_list)) :
        print(solution(s_list[i]))
        print("")

    