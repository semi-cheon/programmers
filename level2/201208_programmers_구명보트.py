# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.08.T
# 문제: 구명보트
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = len(people)
    
    people.sort(reverse=True)
    
    start, end = 0, len(people)-1
    
    while start < end :
        if people[start] + people[end] <= limit:
            end -= 1
            answer -= 1
        start += 1
        
    return answer

if __name__ == "__main__" :
    p_list = [[70,50,80,50],[70,80,50]]
    l_list = [100,100]
    for i in range(len(p_list)) :
        print(solution(p_list[i],l_list[i]))
        print("")
