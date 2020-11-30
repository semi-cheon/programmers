# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.25.W
# 문제: 땅따먹기
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    
    # 동적 계획법
    for i in range(len(land)-1):
        land[i+1][0] = max(land[i][1], land[i][2], land[i][3]) + land[i+1][0]
        land[i+1][1] = max(land[i][0], land[i][2], land[i][3]) + land[i+1][1]
        land[i+1][2] = max(land[i][0], land[i][1], land[i][3]) + land[i+1][2]
        land[i+1][3] = max(land[i][0], land[i][1], land[i][2]) + land[i+1][3]
    
    return max(land[-1])

if __name__ == "__main__" :
    land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
    # for i in range(len(str_list)) :
    print("{} 땅따먹기 최고점은? : {}".format(land, solution(land)))
    print("")
