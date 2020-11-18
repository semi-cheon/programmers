# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.18.W
# 문제: 소수 찾기

### 문제 설명
### 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

### 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
### (1은 소수가 아닙니다.)

### 제한 조건
### n은 2이상 1000000이하의 자연수입니다.

### 입출력 예
### n	result
### 10	4
### 5	3

### 입출력 예 설명
### 입출력 예 #1
### 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

### 입출력 예 #2
### 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환

def solution(n):
    # 효율성 실패
    answer = 0
    for i in range(2, n+1):
        cnt = 0
        for j in range(i,0,-1) :
            if i%j == 0 :
                cnt+=1
        if cnt == 2 :
            answer+=1
    return answer

def solution2(n):
    a = set([i for i in range(3, n+1, 2)]) # 홀수만 추출
    for i in range(3, n+1, 2) :
        if i in a :
            a -= set([i for i in range(i*2, n+1, i)])
    return len(a)+1 # 소수 2 포함

if __name__ == "__main__" :
    n = input('prime number\'s count from 1 to n: ')
    print(solution2(int(n)))
    print()
