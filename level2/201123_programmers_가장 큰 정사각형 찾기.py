# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.20.F
# 문제: 가장 큰 정사각형 찾기
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    zero_check = 0
    for row in board :
        zero_check += sum(row)
    if zero_check == 0 : 
        return 0
    
    answer = 1
    for i in range(1, len(board)) :
        for j in range(1, len(board[0])) :
            if board[i][j] == 0 : 
                continue
            board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1]) + 1
            if board[i][j] > answer :
                answer = board[i][j]
    
    return answer ** 2
 
if __name__ == "__main__" :
    board_list = [[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]], [[0,0,1,1],[1,1,1,1]]]
    for i in range(len(board_list)) :
        solution(board_list[i])
        print("")
