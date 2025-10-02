_msg = "Wrong answer."


def judge(a, b):
    return "Correct" if len(a) == len(b) and all(i == j for i, j in zip(a, b)) else _msg
