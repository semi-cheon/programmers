# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.27.F
# 문제: 행렬의 곱셈
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    
    return [[sum(a * b for a, b in zip(arr1_row,arr2_col)) 
             for arr2_col in zip(*arr2)] 
            for arr1_row in arr1]
 
if __name__ == "__main__" :
    A_list = [ [[1, 4], [3, 2], [4, 1]],  [[2, 3, 2], [4, 2, 4], [3, 1, 4]] ]		
    B_list = [ [[3, 3], [3, 3]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]] ]
    
    for i in range(len(A_list)) :
        print("{}, {} 두 행렬의 곱은 : {}".format(A_list[i], B_list[i], solution(A_list[i], B_list[i])))
        print("")
