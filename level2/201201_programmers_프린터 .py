# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.01.T
# 문제: 프린터
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    
    max_p = max(priorities)
    
    while True:
        value = priorities.pop(0)
        if max_p == value :
            answer += 1
            if location == 0 :
                break
            else :
                location -= 1
            max_p = max(priorities)
        else :
            priorities.append(value)
            if location == 0 :
                location = len(priorities) -1 
            else :
                location -= 1 
    return answer

if __name__ == "__main__" :
    arr_list = [
        [2,1,3,2],
        [1,1,9,1,1,1]
    ]
    location_list = [2, 0]

    for i in range(len(arr_list)) :
        print(solution(arr_list[i], location_list[i]))
        print("")
