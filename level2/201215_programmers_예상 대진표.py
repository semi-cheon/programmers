# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.16.T
# 문제: 예상 대진표
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n, a, b):
    answer = 0
    while a != b:
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
    return answer


if __name__ == "__main__" :  
    
    # for i in range(len(n)) :
    print(solution(8,4,7))
    print("")

    