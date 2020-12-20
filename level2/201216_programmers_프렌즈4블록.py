# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.16.W
# 문제: 프렌즈4블록
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/17679

def delete_sq(m, n, board_T):
    del_set = set()
    
    for i in range(n-1):
        for j in range(m-1):
            if board_T[i][j] == board_T[i][j+1] == board_T[i+1][j] == board_T[i+1][j+1] != '_':
                del_set |= set([(i, j), (i, j+1), (i+1, j), (i+1, j+1)])
    
    for i, j in del_set:
        board_T[i][j] = 0        
    for i, row in enumerate(board_T):
        empty = ['_'] * row.count(0)
        board_T[i] = empty + [block for block in row if block != 0]
    return len(del_set)
     
def solution(m, n, board):
    count = 0
    board_T = list(map(list,zip(*board)))
    while True:
        del_cnt = delete_sq(m, n, board_T)
        if del_cnt == 0: 
            return count
        count += del_cnt

if __name__ == "__main__" :  
    
    n_list = [5,6]
    m_list = [4,6]
    board_list = [['CCBDE', 'AAADE', 'AAABF', 'CCBBF'], 
                ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']]
    for i in range(len(n_list)) :
        print(solution(m_list[i], n_list[i], board_list[i]))
        print("")

    