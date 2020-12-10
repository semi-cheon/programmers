# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.10.T
# 문제: 괄호 변환
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    
    def rule2(p) :
        openc = 0
        closec = 0
        
        for i in range(len(p)) :
            if p[i] == '(' :
                openc += 1
            else :
                closec += 1 
            if openc == closec : 
                return p[:i+1], p[i+1:]
    
    
    def check(u) :
        stack = []
        
        for s in u :
            if s == '(' :
                stack.append(p) 
            else :
                if not stack :
                    return False
                stack.pop()
                
        return True
    
    
    if not p : # rule 1
        return ''
    
    u, v = rule2(p) 

    if check(u) :
        return u + solution(v)
    
    else :
        answer = '('  # rule 4-1
        answer += solution(v) # rule 4-2
        answer += ')'   # rule 4-3
        
        for p in u[1:-1]:
            if p == '(':
                answer += ')'
            else :
                answer += '('
    
        return answer



if __name__ == "__main__" :
    p_list = ["(()())()", ")(", "()))((()"]
    for i in range(len(p_list)) :
        print(solution(p_list[i]))
        print("")

