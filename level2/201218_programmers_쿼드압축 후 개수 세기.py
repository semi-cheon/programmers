# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.18.F
# 문제: 쿼드 압축 후 개수 세기
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def comp(x, y, n):
        init = arr[x][y]  
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:  
                    nn = n // 2
                    comp(x, y, nn)
                    comp(x, y + nn, nn)
                    comp(x + nn, y, nn)
                    comp(x + nn, y + nn, nn)
                    return

        answer[init] += 1

    comp(0, 0, N)
    return answer


if __name__ == "__main__" :  
    arr_list = [[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
                , [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
    ]
    for i in range(len(arr_list)) :
        print(solution(arr_list[i]))
        print("")

    