# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.21.S
# 문제: 실패율
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42889

def solution2(N, stages):
    # 효율성 실패
    answer = []
    stager = [stages.count(i) for i in range(1, N+1)]
    clearer = [len(stages) - sum(stager[:i])for i in range(N)]
    
    ratio = [stager[i]/clearer[i] for i in range(N)]
    
    for i in range(N) :
        answer.append(ratio.index(max(ratio))+1)
        ratio[ratio.index(max(ratio))] = -1
    
    return answer


def solution(N, stages) :
    def solution(N, stages):
    # 스테이지별 도달한 사람의 수
        answer = []
        
        stager = [stages.count(i) for i in range(1, N+1)]
        ratio = [ stages.count(i+1)/(len(stages) - sum(stager[:i])) if stager[i] != 0 else 0.0  for i in range(N)]
            
        answer= dict(sorted([(i+1,ratio[i]) for i in range(len(ratio))], key=(lambda x:x[1]), reverse=True))
        answer = list(answer.keys())
        
        return answer


if __name__ == "__main__" :
    n_list = [5, 4]
    stages_list = [[2, 1, 2, 6, 2, 4, 3, 3], [4,4,4,4,4]]
    for i in range(len(n_list)):
        print("실패율이 가장 높은 스테이지 순서는? {}".format(solution2(n_list[i], stages_list[i])))
        print()
