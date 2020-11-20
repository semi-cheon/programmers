# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.20.F
# 문제: 내적

### 문제 설명
### 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

### 이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

### 제한사항
### a, b의 길이는 1 이상 1,000 이하입니다.
### a, b의 모든 수는 -1,000 이상 1,000 이하입니다.

### 입출력 예
### a	        b	        result
### [1,2,3,4]	[-3,-1,0,2]	3
### [-1,0,1]	[1,0,-1]	-2

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

if __name__ == "__main__" :
    a_list = [[1,2,3,4] , [-1,0,1]]
    b_list = [[-3,-1,0,2], [1,0,-1]]
    for i in range(len(a_list)):
        print("{} 와 {}의 내적은 {}".format(a_list[i], b_list[i], solution(a_list[i], b_list[i])))
        print()
