# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.16.M
# 문제: 가운데 글자 가져오기

### 설명
### 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

### 제한 조건
### s는 길이가 1 이상, 100이하인 스트링입니다.

### 입출력 예
### s	    return
### abcde	c
### qwer	we

def solution(s):
    if len(s) % 2 == 0 :
        answer = s[(len(s)//2)-1:len(s)//2+1]
    else :
        answer = s[len(s)//2]
    return answer

if __name__ == "__main__" :
    a = input("want to find center? ")

    print("center of '"+a+"' :" + solution(a))