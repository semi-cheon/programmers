# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.19.T
# 문제: 제일 작은 수 제거하기

### 문제 설명
### 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

### 제한 조건
### arr은 길이 1 이상인 배열입니다.
### 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

### 입출력 예
### arr	        return
### [4,3,2,1]	[4,3,2]
### [10]	    [-1]

def solution(arr):
    arr.remove(min(arr)) # 가장 작은 값 1개 만 지우기 때문에 중복일 경우 별도 처리 필요
    return arr if len(arr) != 0 else [-1]

if __name__ == "__main__" :
    arr_list = [[4,3,2,1], [10], [4,4,2,2]]
    for arr in arr_list:
        print("{} -> {}".format(arr, solution(arr)))
        print()
