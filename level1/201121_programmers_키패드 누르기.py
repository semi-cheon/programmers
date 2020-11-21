# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.21.S
# 문제: 키패드 누르기
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    locations = {"L":'*', "R":'#'}
    dist = {'L':0 , 'R':0}
    for n in numbers :
        if n in [1,4,7,"*"]:    # click L
            answer += 'L'
            locations['L'] = n 
        elif n in [3,6,9,"#"]:  # click R
            answer += 'R'
            locations['R'] = n 
        else :   
            if locations['L'] in [1,4,7,'*']:
                dist['L'] = abs([2,5,8,0].index(n) - [1,4,7,'*'].index(locations['L'])) + 1                
            elif locations['L'] in [2,5,8,0] :
                dist['L'] = abs([2,5,8,0].index(n) - [2,5,8,0].index(locations['L']))
            
            if locations['R'] in [3,6,9,"#"]:
                dist['R'] = abs([2,5,8,0].index(n) - [3,6,9,"#"].index(locations['R'])) + 1 
                
            elif locations['R'] in [2,5,8,0] :
                dist['R'] = abs([2,5,8,0].index(n) - [2,5,8,0].index(locations['R']))
                
            if dist['R'] > dist["L"] :
                # click L
                answer += 'L'
                locations['L'] = n 
            if dist['R'] < dist["L"] :
                # click R           
                answer += 'R'
                locations['R'] = n      
            if dist['R'] == dist["L"] :
                # click hand
                answer += hand[0].upper()
                locations[hand[0].upper()] = n
    return answer

if __name__ == "__main__" :
    numbers_list = [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	,[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
    hands_list = ['right', 'left', 'right']
    for i in range(len(numbers_list)) :
        print("{}를 순서대로 누르기 위한 키패드를 누르는 손은? {}".format((numbers_list[i]), solution(numbers_list[i], hands_list[i])))
        print()
