# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.02.W
# 문제: 다리를 지나는 트럭
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    sec = 0
    while bridge :
        bridge.pop(0)
        sec += 1
        if truck_weights :
            if (sum(bridge) + truck_weights[0]) <= weight :
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return sec

if __name__ == "__main__" :
    bl_list = [2,100,100]
    w_list = [10,100,100]
    tw_list = [[7,4,5,6],[10],[10,10,10,10,10,10,10,10,10,10]]

    for i in range(len(bl_list)) :
        print(solution(bl_list[i], w_list[i], tw_list[i]))
        print("")
