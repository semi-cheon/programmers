# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.16.T
# 문제: 뉴스 클러스터링
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/17677

import re

def solution(str1, str2):
    str1 = [str1[i:i+2].upper() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].upper() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    inter = set(str1) & set(str2)
    uni = set(str1) | set(str2)
    
    if len(uni) == 0 :
        return 65536

    inter_cnt = sum([min(str1.count(i), str2.count(i)) for i in inter])
    uni_cnt = sum([max(str1.count(u), str2.count(u)) for u in uni])

    return int((inter_cnt/uni_cnt)*65536)
if __name__ == "__main__" :
    str1 = 'FRANCE, handshake, aa1+aa2, E=M*C^2'.split(', ')
    str2 = "french, shake hands, AAAA12, e=m*c^2".split(', ')    
    
    for i in range(len(str1)) :
        print(solution(str1[i], str2[i]))
        print("")

    