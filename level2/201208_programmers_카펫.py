# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.08.T
# 문제: 카펫
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    # total_area = row * col
    # yellow_area = (row-2)*(col-2)
    # brown_area = total_area - yellow_area 
    
    area = brown + yellow  
    row_col = (brown + 4)//2 
    
    if row_col % 2 == 0 :
        row = row_col // 2 
        col = row_col // 2
    else :
        row = row_col // 2 + 1
        col = row_col // 2
        
    for i in range(row_col) :
        if row * col == area:
            return [row, col]
        row += 1
        col -= 1
    return [row, col]

if __name__ == "__main__" :
    b_list = [10,8,24]
    y_list = [2,1,24]

    for i in range(len(b_list)) :
        print(solution(b_list[i], y_list[i]))
        print("")
