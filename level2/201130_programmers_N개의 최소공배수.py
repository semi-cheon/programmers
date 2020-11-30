# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.30.M
# 문제: N개의 최소공배수
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    
    def lcm(n, m) :
        if n % m == 0 :return m
        else :
            return lcm(m, (n % m))
    
    answer = 1 
    for i in arr :
        answer = (answer * i)/lcm(answer , i)
        
    return answer


if __name__ == "__main__" :
    arr_list = [
        [2,6,8,14] ,
        [1,2,3]
    ]
    
    for i in range(len(arr_list)) :
        print("{} 's lcm = {}".format(arr_list[i], solution(arr_list[i])))
        print("")
