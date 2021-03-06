# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.20.F
# 문제: x만큼 간격이 있는 n개의 숫자

### 문제 설명
### 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

### 제한 조건
### x는 -10000000 이상, 10000000 이하인 정수입니다.
### n은 1000 이하인 자연수입니다.

### 입출력 예
### x	n	answer
### 2	5	[2,4,6,8,10]
### 4	3	[4,8,12]
### -4	2	[-4, -8]

def solution(x, n):
    return [x+(x*i) for i in range(n)]

if __name__ == "__main__" :
    x = [2,4,-4]
    n = [5,3,2]
    for i in range(len(x)):
        print("{}만큼 간격이 있는 {}개의 숫자는? {}".format(x[i], n[i], solution(x[i], n[i])))
        print()
