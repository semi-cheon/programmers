# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.18.F
# 문제: 파일명 정렬
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/17686

import re
import pandas as pd

def solution(files):
    file_names = []
    for f in files :
        # print(f)
        heads = [(i.start(), i.end()) for i in re.finditer(r'^[a-zA-Z -]+', f)][0]
        nums = [(i.start(), i.end()) for i in re.finditer(r'[0-9]+', f)][0]
        file_names.append([f, f[heads[0]:heads[1]].lower(), f[nums[0]:nums[1]], f[nums[1]:].lower()])
    df = pd.DataFrame(file_names,columns = ['FILENM', 'HEAD', 'NUMBER', 'TAIL'])
    df.NUMBER = df.NUMBER.astype(int)
    df = df.sort_values([ 'HEAD', 'NUMBER'])
    # print(list(df.FILENM.values))
    answer = list(df.FILENM.values)
    return answer


if __name__ == "__main__" :  
    files_list = [['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
                ,['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']]
    for i in range(len(files_list)) :
        print(solution(files_list[i]))
        print("")

    