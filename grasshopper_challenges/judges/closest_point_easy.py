_msg = "Wrong Answer"


def judge_p(a, b):
    return "Correct" if a.CompareTo(b) == 0 else (_msg)


def judge_i(a, b):
    return "Correct" if a == b else (_msg)


def judge_d(a, b):
    return "Correct" if a == b else (_msg)
