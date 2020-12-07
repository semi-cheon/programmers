# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.07.M
# 문제: H-Index
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort()
    for i in range(len(citations)) :
        if citations[i] >= len(citations) -i:
            return len(citations) -i
    return 0 

if __name__ == "__main__" :
    n_list = [3,0,6,1,5]

    # for i in range(len(n_list)) :
    print(solution(n_list))
    print("")
