# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.17.T
# 문제: 압축
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    total = [chr(i) for i in range(65,91)]
    answer = []
    temp = ''
    for i in msg:
        temp += i
        if temp not in total:
            total.append(temp)
            answer.append(total.index(temp[:-1]))
            temp = temp[len(temp)-1:]

    if temp:
        answer.append(total.index(temp))
    return [i+1 for i in answer]

if __name__ == "__main__" :  
    
    # for i in range(len(n)) :
    print(solution('TOBEORNOTTOBEORTOBEORNOT'))
    print("")

    