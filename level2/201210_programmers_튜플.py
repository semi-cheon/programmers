# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.10.T
# 문제: 튜플
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    
    s = s[2:-2] 
    s = s.split('},{')
    
    s.sort(key = len)
    
    for i in s :
        j = i.split(',')
        for k in j :
            if int(k) not in answer :
                answer.append(int(k))
                
    return answer 



if __name__ == "__main__" :
    s_list = ["{{2},{2,1},{2,1,3},{2,1,3,4}}", 
                "{{1,2,3},{2,1},{1,2,4,3},{2}}",
                "{{20,111},{111}}",
                "{{123}}",
                "{{4,2,3},{3},{2,3,4,1},{2,3}}"]

    for i in range(len(s_list)) :
        print(solution(s_list[i]))
        print("")

    