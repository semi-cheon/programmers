# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.21.S
# 문제: 비밀지도
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    # bin(i|j) [2:]
    
    pw_arr1 = [bin(i)[2:].rjust(n, ' ').replace("1", "#").replace("0", " ") for i in arr1 ]
    pw_arr2 = [bin(i)[2:].rjust(n, ' ').replace("1", "#").replace("0", " ") for i in arr2 ]
    
    answer = ["".join(["#" if pw_arr1[i][j] == "#" or pw_arr2[i][j] == '#' else " " for j in range(n)])
                for i in range(len(arr1))]
                
    return answer

if __name__ == "__main__" :
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]

    print("지도는? {}".format(solution(n, arr1, arr2)))
    print()
