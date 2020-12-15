# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.16.T
# 문제: 영어 끝말잇기
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]
    count = 1 
    for idx in range(1, len(words)): 
        word = words[idx] 
        count %= n 
        if (word in words[0:idx]) or (words[idx-1][-1] != word[0]): 
            answer = [count +1, 1 + idx//n]
            return answer 
        count +=1 
    return answer

if __name__ == "__main__" :
    n = [3,5,2]
    s = ["tank, kick, know, wheel, land, dream, mother, robot, tank".split(', ')
        , "hello, observe, effect, take, either, recognize, encourage, ensure, establish, hang, gather, refer, reference, estimate, executive".split(', ')
        , "hello, one, even, never, now, world, draw".split(', ')]
        
    
    for i in range(len(n)) :
        print(solution(n[i], s[i]))
        print("")

    