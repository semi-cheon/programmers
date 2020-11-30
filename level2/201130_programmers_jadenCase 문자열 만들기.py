# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.30.M
# 문제: JadenCase 문자열 만들기
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    # s.title()
    return " ".join([i.capitalize() for i in s.split(" ")]) 

if __name__ == "__main__" :
    s_list = ['3people unFollowed me', 'for the last week']
    
    for i in range(len(s_list)) :
        print("{} to jadenCase -> {}".format(s_list[i], solution(s_list[i])))
        print("")
