# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.02.W
# 문제: 기능개발
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    day = []
    for i in range(len(progresses)) :
        n = 0
        while progresses[i] + (n * speeds[i]) < 100 :
            n += 1
        day.append(n)
    n = 1
    while day :
        if len(day) == 1 :
            answer.append(n)
            break
        if day[0] >= day[1] :
            day[1] = day[0]
            day.pop(0)
            n += 1
        else :
            answer.append(n)
            day.pop(0)
            n = 1
    return answer

if __name__ == "__main__" :
    p_list = [[93,30,55],[95,90,99,99,80,99]]
    s_list = [[1,30,5],[1,1,1,1,1,1]]
    
    for i in range(len(p_list)) :
        print(solution(p_list[i], s_list[i]))
        print("")
