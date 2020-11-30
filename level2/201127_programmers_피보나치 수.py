# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.27.F
# 문제: 피보나치 수
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    
    fib = []
    # 재귀함수는 런타임, 시간 초과
    # simple is the best
    for i in range(0, n) :
        if i < 2 :
            fib.append(1)
        else :
            fib.append(fib[i-1]+fib[i-2])
            
    if n>=2 :
        return fib[n-1] % 1234567
 
if __name__ == "__main__" :
    n_list = [3,5]
    for i in range(len(n_list)) :
        print("{}번째 피보나치수를 1234567로 나눈 나머지는 : {}".format(n_list[i], solution(n_list[i])))
        print("")
