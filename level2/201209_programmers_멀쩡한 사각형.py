# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.09.W
# 문제: 멀쩡한 사각형
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/62048

import math
def solution(w,h):
    return w * h - (w + h - math.gcd(w, h))



if __name__ == "__main__" :
    w_list = [8]
    h_list = [12]
    for i in range(len(w_list)) :
        print(solution(w_list[i], h_list[i]))
        print("")
