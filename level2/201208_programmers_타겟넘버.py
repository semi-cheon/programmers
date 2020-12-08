# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.08.T
# 문제: 타겟넘버
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    super = [0]
    
    for i in numbers :
        temp = []
        for j in super:
            temp.append(j + i)
            temp.append(j - i)
        super = temp
    
    return super.count(target)

if __name__ == "__main__" :
    n_list = [[1,1,1,1,1]]
    t_list = [3]
    for i in range(len(n_list)) :
        print(solution(n_list[i], t_list[i]))
        print("")
