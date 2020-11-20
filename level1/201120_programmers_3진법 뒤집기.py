# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.20.F
# 문제: 3진법 뒤집기

### 문제 설명
### 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

### 제한사항
### n은 1 이상 100,000,000 이하인 자연수입니다.

### 입출력 예
### n	result
### 45	7
### 125	229

def solution(n):
    
    def convert(n, base):   
        T = "0123456789ABCDEF"  
        q, r = divmod(n, base)
        if q == 0:
            return T[r]
        else:
            return convert(q, base) + T[r]
    
    n3 = convert(n, 3)   
    answer = 0 
    i = 0
    
    for s in str(n3):
        answer += (int(s) * (3 ** i))
        i+=1
    
    return answer

if __name__ == "__main__" :
    arr_list = [45, 125]
    for arr in arr_list:
        print("{}를 3진법으로 만들어 뒤집은 수는 {}".format(arr, solution(arr)))
        print()
