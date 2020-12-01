# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.01.T
# 문제: 주식가격
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    for i in range(len(prices)-1): 
        count = 0
        for j in range(i+1, len(prices)): 
            if (j == len(prices) - 1 or prices[i] > prices[j]): 
                answer.append(count+1)
                break
            else : 
                count +=1
    answer += [0]
    return answer

if __name__ == "__main__" :
    stock_list = [[1, 2, 3, 2, 3]]
    for i in range(len(stock_list)) :
        print("{} 주식가격이 떨어지지 않은 초는 {} ".format(stock_list[i], solution(stock_list[i])))
        print("")
