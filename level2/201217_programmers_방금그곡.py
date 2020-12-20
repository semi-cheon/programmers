# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.17.T
# 문제: 방금그곡
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    def change_tune(m):
        m = m.replace('C#', 'c')
        m = m.replace('D#', 'd')
        m = m.replace('F#', 'f')
        m = m.replace('G#', 'g')
        m = m.replace('A#', 'a')
        return m
    answer = '(None)'
    answer_t = -1
    for musics in musicinfos :
        start, end, title, music = musics.split(',')
        times = (int(end[:2]) - int(start[:2])) * 60 + (int(end[-2:]) - int(start[-2:]))
        m = change_tune(m)
        music = change_tune(music) 
        print(music*times)
        played = (music*times)[:times]
        
        if m in played :
            if (answer == -1) or (times > answer_t):
                answer, answer_t = title, times
                
    return answer

if __name__ == "__main__" :  
    m_list = ['ABCDEFG', 'CC#BCC#BCC#BCC#B', 'ABC']
    mi_list = [['12:00,12:14,HELLO,CDEFGAB', "13:00,13:05,WORLD,ABCDEF"]
                , ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']
                , ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']]
    for i in range(len(m_list)) :
        print(solution(m_list[i], mi_list[i]))
        print("")

    