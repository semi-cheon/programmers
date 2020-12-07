# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.07.M
# 문제: 전화번호 목록
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    
    for p in phone_book:
        for p2 in phone_book:
            if p != p2 :
                if p2.startswith(p) :
                    return False 
                
    return answer

if __name__ == "__main__" :
    p_list = [['119', '97674223', '1195524421'],	
                ['123','456','789'],	
                ['12','123','1235','567','88']]

    for i in range(len(p_list)) :
        print(solution(p_list[i]))
        print("")
