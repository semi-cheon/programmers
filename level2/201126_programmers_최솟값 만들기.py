# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.26.T
# 문제: 최솟값 만들기
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0  
    
    # list에서 가장 큰 수와 작은 수를 차례로 곱해서 더하면 합이 제일 작다.
    A = sorted(A)
    B = sorted(B)
    
    for i in range(len(A)) :
        answer += A[i] * B[(i+1)*(-1)]

    return answer
 
if __name__ == "__main__" :
    A_list = [[1,4,2], [1,2]]
    B_list = [[5,4,4], [3,4]]
    for i in range(len(A_list)) :
        print("{}와 {}의 곱의 합이 최소가 되는 값은 : {}".format(A_list[i], B_list[i], solution(A_list[i], B_list[i])))
        print("")

