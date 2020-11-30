# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.24.T
# 문제: 다음 큰 숫자
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    
    big_n = n + 1 
    while(bin(n).count("1") != bin(big_n).count("1")) :
        big_n += 1
        
    return big_n

if __name__ == "__main__" :
    n_list = [78, 15]
    for i in range(len(n_list)) :
        print("{}의 다음 큰 숫자는: {}".format(n_list[i], solution(n_list[i])))
        print("")
