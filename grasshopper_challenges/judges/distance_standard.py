_msg = "Wrong: Expected {} but got {}."


def judge(a, b):
    return "Correct" if a == b else (_msg.format(a, b))
