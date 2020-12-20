# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.17.T
# 문제: 예상 대진표
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12985


def solution(n, t, m, p):
    
    def convert(n, base):   
        T = "0123456789ABCDEF"  
        q, r = divmod(n, base)
        if q == 0:
            return T[r]
        else:
            return convert(q, base) + T[r]    
        
    numbers_list = [convert(i, n) for i in range(t*m+p)]
    
    
    return ''.join(numbers_list)[p-1:m*t:m]


if __name__ == "__main__" :  
    n_list = [2,16,16]
    t_list = [4,16,16]
    m_list = [2,2,2]
    p_list = [1,1,2]
    for i in range(len(n_list)) :
        print(solution(n_list[i], t_list[i], m_list[i], p_list[i]))
        print("")

    