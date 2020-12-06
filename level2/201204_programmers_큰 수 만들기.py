# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.04.F
# 문제: 큰 수 만들기
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    numbers = []
    
    for i, n in enumerate(number) :
        while len(numbers) > 0 and numbers[-1] < n and k > 0 :
            numbers.pop()
            k -= 1
        if k == 0 :
            numbers += list(number[i:])
            break
        numbers.append(n)
    numbers = numbers[:-k] if k > 0 else numbers
    
    return "".join(numbers)


if __name__ == "__main__" :
    n_list = ['1924', '1231234', '4177252841']
    k_list = [2,3,4]

    for i in range(len(n_list)) :
        print(solution(n_list[i], k_list[i]))
        print("")
