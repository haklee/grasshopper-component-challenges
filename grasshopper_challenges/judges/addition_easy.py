_msg = "Wrong: Sum of {} and {} is not equal to {}."


def judge(a, b, c):
    return "Correct" if a == b else (_msg.format(a, b, c))
