_msg = "Wrong: Absolute value of {} is not equal to {}."


def judge(a, b):
    return "Correct" if a == b else (_msg.format(a, b))
