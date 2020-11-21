# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.21.S
# 문제: 크레인 인형뽑기 게임
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    pop_list = []
    for m in moves :
        for i in range(len(board)) :
            if board[i][m-1] != 0 :
                pop_list.append(board[i][m-1])
                board[i][m-1] = 0
                break
        if len(pop_list) >= 2:
            if pop_list[-1] == pop_list[-2]:
                pop_list = pop_list[:-2]
                answer += 2
    return answer

if __name__ == "__main__" :
    print("터트려진 인형의 갯수는? {}".format(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])))
    print()
