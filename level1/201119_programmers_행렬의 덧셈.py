# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.19.T
# 문제: 행렬의 덧셈

### 문제 설명
### 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

### 제한 조건
### 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

### 입출력 예
### arr1	        arr2	        return
### [[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
### [[1],[2]]	    [[3],[4]]	    [[4],[6]]

def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        r = []
        for j in range(0, len(arr1[0])):
            r.append(arr1[i][j] + arr2[i][j])
        answer.append(r)
    return answer

if __name__ == "__main__" :
    arr1_list = [[[1,2],[2,3]], [[1],[2]]]
    arr2_list = [[[3,4],[5,6]], [[3],[4]]]
    for i in range(len(arr1_list)): 
        print("{} + {} = {}".format(arr1_list[i], arr2_list[i], solution(arr1_list[i], arr2_list[i])))
        print()
