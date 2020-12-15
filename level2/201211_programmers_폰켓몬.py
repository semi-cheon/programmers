# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.11.F
# 문제: 폰켓몬
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/1845


from itertools import combinations

# 조합 추출 -- 시간 초과
# def solution(nums):
#     combies = combinations("".join([str(i) for i in nums]), len(nums)//2)
#     return max([len(set(c)) for c in list(combies)])

def solution(nums):   
    if len(set(nums)) >= len(nums)//2 :
        return len(nums)//2
    else :
        return len(set(nums))
    

if __name__ == "__main__" :
    n_list = [[3,1,2,3]
            , [3,3,3,2,2,4]
            , [3,3,3,2,2,2]]
    
    for i in range(len(n_list)) :
        print(solution(n_list[i]))
        print("")

    