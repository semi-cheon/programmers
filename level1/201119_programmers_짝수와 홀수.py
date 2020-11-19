# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.19.T
# 문제: 짝수와 홀수

### 문제 설명
### 정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.

### 제한 조건
### num은 int 범위의 정수입니다.
### 0은 짝수입니다.

### 입출력 예
### num	return
### 3	Odd
### 4	Even

def solution(num):
    return "Even" if num % 2 == 0 else "Odd"

if __name__ == "__main__" :
    num_list = [3, 4]
    for num in num_list :
        print("{} is {}".format(num, solution(num)))
        print()
