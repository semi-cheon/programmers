# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.20.F
# 문제: 124 나라의 숫자
# 문제 url : https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    def convert(n, base):   
        T = "0124"  
        q, r = divmod(n-1, base)
        if q == 0 :
            return T[r+1]
        else :
            return convert(q, base) + T[r+1]

    answer = convert(n, 3)
    return answer
    

if __name__ == "__main__" :
    for i in range(1,11) :
        print(i, solution(i))