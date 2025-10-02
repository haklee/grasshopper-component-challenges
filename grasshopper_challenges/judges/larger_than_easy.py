from .helper.comparer import compare_bool

_msg = "Wrong Answer"


def judge_gt(a, b):
    return "Correct" if compare_bool(a, b) else (_msg)


def judge_ge(a, b):
    return "Correct" if compare_bool(a, b) else (_msg)
