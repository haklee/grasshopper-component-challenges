_msg = "Wrong: vector {} is not equal to {}."


def judge(a, b):
    return "Correct" if a.CompareTo(b) == 0 else (_msg.format(a, b))
