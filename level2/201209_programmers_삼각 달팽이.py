# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.09.W
# 문제: 삼각 달팽이
# 문제 url:https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    li = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            li[x][y] = num
            num += 1
    for i in li:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer



if __name__ == "__main__" :
    n_list = [4,5,6]
    for i in range(len(n_list)) :
        print(solution(n_list[i]))
        print("")

