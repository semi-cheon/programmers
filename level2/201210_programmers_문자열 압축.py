# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.10.T
# 문제: 문자열 압축
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    length = []
    result = ""
    
    if len(s) == 1:
        return 1
    
    for c in range(1, len(s) // 2 + 1): 
        cnt = 1
        tempStr = s[:c] 
        for i in range(c, len(s), c):
            if s[i:i+c] == tempStr:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                result += str(cnt) + tempStr
                tempStr = s[i:i+c]
                cnt = 1

        if cnt == 1:
            cnt = ""
        result += str(cnt) + tempStr
        length.append(len(result))
        result = ""
    
    return min(length)



if __name__ == "__main__" :

    s_list = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
    
    for i in range(len(s_list)) :
        print(solution(s_list[i]))
        print("")

