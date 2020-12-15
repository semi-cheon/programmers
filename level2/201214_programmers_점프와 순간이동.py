# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.14.M
# 문제: 점프와 순간이동
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    return bin(n)[2:].count("1")
    

if __name__ == "__main__" :
    s_list = [5,6,5000]
    
    for i in range(len(s_list)) :
        print(solution(s_list[i]))
        print("")

    