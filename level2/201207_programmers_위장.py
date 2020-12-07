# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.07.M
# 문제: 위장
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    dressup = dict() 
    answer = 1
    
    for i in range(len(clothes)) :
        if hash(clothes[i][1]) in dressup:
            dressup[hash(clothes[i][1])] += 1
        else :
            dressup[hash(clothes[i][1])] = 1
    
    for v in dressup.values() :
        answer *= (v+1)
        
    return answer -1 

if __name__ == "__main__" :
    c_list = [[['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]	,
                [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]]
    for i in range(len(c_list)) :
        print(solution(c_list[i]))
        print("")
