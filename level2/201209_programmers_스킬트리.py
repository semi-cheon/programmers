# python 코딩 테스트 연습
# 작성자: 천세미
# 작성일: 2020.12.09.W
# 문제: 스킬트리
# 문제 url: https://programmers.co.kr/learn/courses/30/lessons/49993


def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        s_list = list(skill)

        for s in skills:
            if s in skill:
                if s != s_list.pop(0):
                    break
        else:
            answer += 1

    return answer


if __name__ == "__main__" :
    skill = "CBD"	
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

    # for i in range(len(n_list)) :
    print(solution(skill, skill_trees))
    print("")

    