# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.24.T
# 문제: 올바른 괄호
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    
    # 효율성 실패
#     def rep_s(s) :
#         return s.replace('()', '')
    
#     old_s = s 
#     new_s = rep_s(old_s)
#     while(old_s != new_s) :
#         old_s = rep_s(new_s)
#         new_s = rep_s(old_s)
    
#     answer = True if new_s == "" else False
    
    stack = []
    
    for i in s:
        if i == "(":
            stack.append("(")
        elif len(stack) == 0 :
            return False 
        else :
            stack.pop()
            
    if len(stack) > 0 :
        return False
    else :
        return True 

if __name__ == "__main__" :
    str_list = ["()()", "(())()", ")()(", '(()(']
    for i in range(len(str_list)) :
        print("{}는 올바른 괄호쌍인가요? : {}".format(str_list[i], solution(str_list[i])))
        print("")
