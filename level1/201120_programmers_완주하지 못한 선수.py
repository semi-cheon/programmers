# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.20.F
# 문제: 완주하지 못한 선수

### 문제 설명
### 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
### 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

### 제한사항
### 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
### completion의 길이는 participant의 길이보다 1 작습니다.
### 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
### 참가자 중에는 동명이인이 있을 수 있습니다.

### 입출력 예
### participant	                            completion	                        return
### [leo, kiki, eden]	                    [eden, kiki]	                    leo
### [marina, josipa, nikola, vinko, filipa]	[josipa, filipa, marina, nikola]	vinko
### [mislav, stanko, mislav, ana]	        [stanko, ana, mislav]	            mislav

def solution(participant, completion):
    dict_part = {}
    for i in participant :
        if i in dict_part.keys() :
            dict_part[i] += 1 
        else :
            dict_part[i] = 1
    
    for i in completion:
        dict_part[i] -= 1 
        
    answer = [k for k in dict_part.keys() if dict_part[k] > 0 ]
    
    return answer[0]

if __name__ == "__main__" :
    participant_list = [['leo', 'kiki', 'eden'], ['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['mislav', 'stanko', 'mislav', 'ana']]
    completion_list = [['kiki', 'eden'], ['marina', 'josipa', 'nikola', 'filipa'], ['mislav', 'stanko', 'ana']]
    for i in range(len(participant_list)):
        print("완주하지 못한 선수는? {}".format( solution(participant_list[i], completion_list[i])))
        print()
