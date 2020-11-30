# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.25.W
# 문제: 숫자의 표현
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    
    for i in range(1, n+1) :
        sum = 0 
        for j in range(i, n+1) :
            sum += j 
            if sum == n :
                answer += 1
                break
            if sum > n :
                break
    return answer

if __name__ == "__main__" :
    n = 15
    # for i in range(len(str_list)) :
    print("{}를 연속한 숫자의 덧셈으로 표현하는 방법은? : {}".format(n, solution(n)))
    print("")
