# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.11.F
# 문제: 이진 변환 반복하기
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = [0, 0]
    while s != '1' :
        answer[0] += 1
        answer[1] += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
    return answer
    

if __name__ == "__main__" :
    s_list = ["110010101001"
            , "01110"
            , "1111111"]
    
    for i in range(len(s_list)) :
        print(solution(s_list[i]))
        print("")

    