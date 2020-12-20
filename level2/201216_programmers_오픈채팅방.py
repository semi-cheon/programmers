# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.16.W
# 문제: 오픈채팅방
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    user = {}
    answer = []
    answer2 = []
    
    for r in record:
        r_list = r.split()
        if len(r_list) != 2 :
            user[r_list[1]] = r_list[2] 
        
        if r_list[0] == 'Enter' :
            answer.append(r_list[1]+'님이 들어왔습니다.')
        elif r_list[0] == 'Leave' :
            answer.append(r_list[1]+'님이 나갔습니다.')
        
    for a in answer :
        answer2.append(a.replace(a[:a.find('님')], user[a[:a.find('님')]]))
    
    return answer2

if __name__ == "__main__" :  
    
    # for i in range(len(n)) :
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
    print("")

    