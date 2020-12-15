# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.11.F
# 문제: 수식 최대화
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
import re

def solution(expression):
    exprs = set(re.findall("\D", expression))
    prior = permutations(exprs)
    cand = []

    for op in prior:
        temp = re.compile("(\D)").split(expression)
        for exp in op:
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]
        cand.append(abs(int(temp[0])))
    return max(cand)
    

if __name__ == "__main__" :
    s_list = ["100-200*300-500+20"
            , "50*6-3*2"]
    
    for i in range(len(s_list)) :
        print(solution(s_list[i]))
        print("")

    