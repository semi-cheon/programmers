# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.03.T
# 문제: 조이스틱
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    names2 = [abs(alphas[::-1].index(n))+1 if abs(alphas.index(n)) > (abs(alphas[::-1].index(n) +1))
                else abs(alphas.index(n)) for n in name]
    
    
    idx, answer = 0, 0 
    while True: 
        answer += names2[idx] 
        names2[idx] = 0 
        
        if sum(names2) == 0: 
            break 
        left, right = 1, 1 
        
        while names2[idx - left] ==0: 
            left +=1 
        
        while names2[idx + right] ==0: 
            right +=1 
            
        answer += left if left < right else right 
        idx += -left if left < right else right 
        
    return answer

if __name__ == "__main__" :
    n_list = ['JEROEN', 'JAN']
    
    for i in range(len(n_list)) :
        print(solution(n_list[i]))
        print("")
