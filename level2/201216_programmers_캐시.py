# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.16.W
# 문제: 캐시
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    cache_list = []
    answer = 0
    cities = [c.upper() for c in cities]
    
    for city in cities :
        if city in cache_list :
            answer += 1
        else :
            answer += 5

        if cacheSize == 0 :
            continue
        elif len(cache_list) < cacheSize:
            if city in cache_list :
                cache_list.remove(city)
                cache_list.append(city)
            else :
                cache_list.append(city)
        else :
            if city in cache_list :
                cache_list.remove(city)
                cache_list.append(city)
            else :    
                cache_list.pop(0)
                cache_list.append(city)
            
    return answer

if __name__ == "__main__" :  

    city_list = [['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
                , ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
                , ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
                , ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
                , ['Jeju', 'Pangyo', 'NewYork', 'newyork']
                , ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']]

    cacheSize_list = [3,3,2,5,2,0]
    for i in range(len(city_list)) :
        print(solution(cacheSize_list[i], city_list[i]))
        print("")

    