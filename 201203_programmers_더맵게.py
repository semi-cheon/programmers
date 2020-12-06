# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.03.T
# 문제: 더 맵게
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def  solution(scoville, k) :
    heap = []
    
    for s in scoville :
        heapq.heappush(heap, s)
        
    cnt = 0
    
    while heap[0] < k :
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError :
            return -1
        cnt += 1
        
    return cnt

if __name__ == "__main__" :
    s_list = [[1,2,3,9,10,12]]
    k_list = [7]
    
    for i in range(len(s_list)) :
        print(solution(s_list[i], k_list[i]))
        print("")
