# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.11.21.S
# 문제: 다트게임
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/17682


def solution(dartResult):

    # re 모듈을 사용해서 해볼 것
    numbers = []
    points = []
    alphas = []
    
    for i in range(len(dartResult)) :
        if dartResult[i].isdigit() :
            if dartResult[i] == '1' :
                if i!=len(dartResult):
                    if dartResult[i+1] == '0' :
                        numbers.append(dartResult[i]+dartResult[i+1])
                    else :
                        numbers.append(dartResult[i])
            elif (dartResult[i-1] == "1") & (dartResult[i] == '0') :
                continue
            else :
                numbers.append(dartResult[i])
        elif dartResult[i] in ["S", 'D', 'T']:
            points.append(dartResult[i])
            if (i!= len(dartResult)-1) :
                if dartResult[i+1].isdigit() :
                    alphas.append(" ")
                else :
                    alphas.append(dartResult[i+1])
            else :
                alphas.append(" ")
    
    points = ['1' if i =='S' else '2' if i=="D" else '3' for i in points ]
    
    alphas_str = [''] * len(alphas)
    
    for i in range(len(alphas)) :
        if i != 0 :
            if alphas[i] == '*' :
                alphas_str[i-1] += "*2"
                alphas_str[i] += '*2'
        elif i== 0 :
            if alphas[i] == '*':
                alphas_str[i] += '*2'
                
        if alphas[i] == "#":
            alphas_str[i] += '*(-1)'
            
    answer = "+".join([numbers[i]+"**"+points[i]+alphas_str[i] for i in range(len(alphas))])
        
    return eval(answer)


if __name__ == "__main__" :
    dartResult_list = ['1S2D*3T','1D2S#10S','1D2S0T','1S*2T*3S','1D#2S*3S','1T2D3D#','1D2S3T*']
    for i in range(len(dartResult_list)):
        print("{}와 같이 맞춘 다트 점수는? {}".format(dartResult_list[i],solution(dartResult_list[i])))
        print()
