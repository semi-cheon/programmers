# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.04.F
# 문제: 가장 큰 수 
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    
    numbers = [str(n) for n in numbers]
    numbers.sort(key = lambda x : x*4, reverse=True)
    
    return str(int("".join(numbers)))


if __name__ == "__main__" :
    n_list = [[6,10,2],[3,30,34,5,9]]
    
    for i in range(len(n_list)) :
        print(solution(n_list[i]))
        print("")
