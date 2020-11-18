# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.18.W
# 문제: 약수의 합

### 문제 설명
### 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

### 제한 사항
### n은 0 이상 3000이하인 정수입니다.

### 입출력 예
### n	return
### 12	28
### 5	6

### 입출력 예 설명
### 입출력 예 #1
### 12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

### 입출력 예 #2
### 5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.


def solution(n):
    divider = []
    for i in range(1, n+1) :
        if n % i == 0 :
            divider.append(i)
    return sum(divider)

if __name__ == "__main__" :
    for i in [12, 5] :
        print('{}의 약수의 합: {}'.format(i, solution(i)))
        print()
