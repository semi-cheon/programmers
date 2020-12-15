# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.15.M
# 문제: 짝지어 제거하기
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []

    for i in s:
        if len(stack) == 0 :
            stack.append(i)
        elif stack[-1] == i :
            stack.pop()
        else :
            stack.append(i)
    
    return 1 if len(stack) == 0 else 0

if __name__ == "__main__" :
    s_list = ["baabaa", 'cdcd']
    
    for i in range(len(s_list)) :
        print(solution(s_list[i]))
        print("")

    