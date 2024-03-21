# Solution 1: Sample Solution
def possible(answer):
    for x, y, type_ in answer:
        # Column
        if type_ == 0:
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or ([x - 1, y, 1] in answer or [x, y, 1] in answer) or [x , y - 1, 0] in answer:
                continue
            return False
        # Beam
        elif type_ == 1:
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y , 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True
            

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, type_, operation = frame
        # Remove
        if operation == 0:
            answer.remove([x, y, type_])
            if not possible(answer):
                answer.append([x, y, type_])
        # Build
        if operation == 1:
            answer.append([x, y, type_])
            if not possible(answer):
                answer.remove([x, y, type_])
    return sorted(answer)