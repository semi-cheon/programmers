# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.26.T
# 문제: 최댓값과 최솟값
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    numbers = ([int(i) for i in s.split(' ')])
    return "{} {}".format(min(numbers), max(numbers)) 
 
if __name__ == "__main__" :
    s_list = ['1 2 3 4', '-1 -2 -3 -4', '-1 -1']
    for i in range(len(s_list)) :
        print("{} 의 최솟값과 최댓값은 : {}".format(s_list[i], solution(s_list[i])))
        print("")
